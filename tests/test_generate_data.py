import unittest
from modules.generate_data import generate_dummy_data

class TestGenerateData(unittest.TestCase):
    def test_generate_dummy_data(self):
        num_rows = 100
        df = generate_dummy_data(num_rows)
        self.assertEqual(len(df), num_rows)
        self.assertTrue('ID' in df.columns)
        self.assertTrue('Name' in df.columns)
        self.assertTrue('Date' in df.columns)
        self.assertTrue('Value' in df.columns)

if __name__ == '__main__':
    unittest.main()
