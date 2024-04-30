import unittest
from modules.generate_data import generate_dummy_data
from modules.transform_data import transform_data

class TestETLPipeline(unittest.TestCase):
    def test_etl_pipeline(self):
        num_rows = 100
        df = generate_dummy_data(num_rows)
        transformed_df = transform_data(df)
        self.assertEqual(len(transformed_df), len(df['ID'].unique()))

if __name__ == '__main__':
    unittest.main()