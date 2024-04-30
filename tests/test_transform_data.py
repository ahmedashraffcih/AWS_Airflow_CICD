import unittest
import pandas as pd
from modules.transform_data import transform_data

class TestTransformData(unittest.TestCase):
    def test_transform_data(self):
        # Create sample DataFrame
        df = pd.DataFrame({
            'ID': [1, 1, 2, 2],
            'Value': [100, 200, 300, 400],
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
        })
        transformed_df = transform_data(df)
        self.assertEqual(len(transformed_df), 2)  # Two unique IDs
        self.assertTrue('ID' in transformed_df.columns)
        self.assertTrue('Total_Value' in transformed_df.columns)
        self.assertTrue('Average_Value' in transformed_df.columns)
        self.assertTrue('Min_Date' in transformed_df.columns)
        self.assertTrue('Max_Date' in transformed_df.columns)
        self.assertTrue('Value_Range' in transformed_df.columns)
        self.assertTrue('Value_Std' in transformed_df.columns)
        self.assertTrue('Value_Category' in transformed_df.columns)

if __name__ == '__main__':
    unittest.main()