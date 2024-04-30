from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from modules.generate_data import generate_dummy_data
from modules.transform_data import transform_data
import boto3

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 30),
    'retries': 1,
}

def save_to_s3(df, bucket_name, key):
    # Save DataFrame to CSV and upload to S3
    csv_buffer = df.to_csv(index=False)
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, key)
    obj.put(Body=csv_buffer)

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline with Airflow',
    schedule_interval='@daily',
)

generate_data_task = PythonOperator(
    task_id='generate_dummy_data',
    python_callable=generate_dummy_data,
    op_kwargs={'num_rows': 1000},
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    op_kwargs={'df': '{{ task_instance.xcom_pull(task_ids="generate_dummy_data") }}'},
    dag=dag,
)

save_to_s3_task = PythonOperator(
    task_id='save_to_s3',
    python_callable=save_to_s3,
    op_kwargs={
        'df': '{{ task_instance.xcom_pull(task_ids="transform_data") }}',
        'bucket_name': 'tf-mwaa-airflow-bucket',
        'key': 'transformed_data.csv'
    },
    dag=dag,
)

generate_data_task >> transform_data_task >> save_to_s3_task
