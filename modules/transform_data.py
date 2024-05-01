import pandas as pd
from airflow.hooks.S3_hook import S3Hook

def transform_data(df):
    # Load CSV file from S3
    s3_hook = S3Hook(aws_conn_id="conn_id")  # Update with your AWS connection ID
    csv_buffer = s3_hook.read_key(key, bucket_name=bucket_name)
    df = pd.read_csv(csv_buffer)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'].fillna('1970-01-01', inplace=True)
    
    grouped_data = df.groupby('ID').agg({
        'Value': ['sum', 'mean'],
        'Date': ['min', 'max']
    }).reset_index()
    
    grouped_data.columns = ['ID', 'Total_Value', 'Average_Value', 'Min_Date', 'Max_Date']
    
    grouped_data['Value_Range'] = grouped_data['Total_Value'] - grouped_data['Average_Value']  # Corrected calculation
    grouped_data['Value_Std'] = df.groupby('ID')['Value'].std()
    
    bins = [-float('inf'), 100, 200, 300, float('inf')]
    labels = ['0-100', '101-200', '201-300', '301+']
    grouped_data['Value_Category'] = pd.cut(grouped_data['Total_Value'], bins=bins, labels=labels)
    
    return grouped_data
