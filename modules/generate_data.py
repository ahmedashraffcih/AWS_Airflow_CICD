from faker import Faker
import pandas as pd

fake = Faker()

def generate_dummy_data(num_rows):
    # Generate dummy data using Faker
    data = {
        'ID': [fake.random_int(min=1, max=100) for _ in range(num_rows)],
        'Name': [fake.name() for _ in range(num_rows)],
        'Date': [fake.date_this_decade() for _ in range(num_rows)],
        'Value': [fake.random_number(digits=5) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)
