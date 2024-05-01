from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from modules.generate_data import generate_dummy_data
from modules.transform_data import transform_data
from airflow.models import Variable
import airflow
from airflow.hooks.S3_hook import S3Hook

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 30),
    'retries': 1,
}
def extract_data(**kwargs):
    print("Extracting started ")
    ti = kwargs['ti']
    df = generate_dummy_data(100)
    return df

def transform_step(df, **kwargs):
    print("Transforming data")
    final_df = transform_data(df)
    return final_df

def save_to_s3(df, bucket_name, key):
    # Save DataFrame to CSV and upload to S3
    csv_buffer = df.to_csv(index=False)
    
    conn_id = Variable.get("aws_connect")  # Assuming you've configured the connection ID in Airflow Variables
    s3_hook = airflow.hooks.S3Hook(conn_id)
    
    # Upload the file to S3
    s3_hook.load_string(
        string_data=csv_buffer,
        key=key,
        bucket_name=bucket_name,
        replace=True
    )

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline with Airflow',
    schedule_interval='@daily',
)

extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    provide_context=True,
    dag=dag,
)

transform_step_task = PythonOperator(
    task_id='transform_step',
    python_callable=transform_step,
    provide_context=True,
    dag=dag,
)

save_to_s3_task = PythonOperator(
    task_id='save_to_s3',
    python_callable=save_to_s3,
    op_kwargs={
        'df': "{{ task_instance.xcom_pull(task_ids='transform_step') }}",
        'bucket_name': 'tf-mwaa-airflow-bucket',
        'key': 'dummy_data.csv'
    },
    dag=dag,
)

extract_data_task >> transform_step_task >> save_to_s3_task
