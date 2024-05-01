import pandas as pd

def transform_data(df):
    df['Date'].fillna('1970-01-01', inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    
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
