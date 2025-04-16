import unittest
from mainclass import SalesDataProcessor
from test.TestUtils import TestUtils
import numpy as np
import pandas as pd


class ExceptionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.invalid_file_path = 'invalid_sales_data.csv'  # A non-existent file path
        self.sales_processor = SalesDataProcessor(self.invalid_file_path)

    def test_invalid_csv_path(self):
        """Test handling of a missing or invalid CSV file."""
        test_obj = TestUtils()
        try:
            self.sales_processor.read_csv()
            test_obj.yakshaAssert("TestInvalidCSVPath", False, "exceptional")
            print("TestInvalidCSVPath = Failed")
        except FileNotFoundError:
            test_obj.yakshaAssert("TestInvalidCSVPath", True, "exceptional")
            print("TestInvalidCSVPath = Passed")

    def test_missing_column(self):
        """Test handling of a missing 'total_sales' column in CSV."""
        # Mocking a DataFrame that doesn't contain the 'total_sales' column
        self.sales_processor.df = pd.DataFrame({
            'product_id': [1, 2, 3],
            'product_name': ['Product A', 'Product B', 'Product C'],
            'units_sold': [10, 20, 30],
            'price': [5, 10, 15]
        })
        test_obj = TestUtils()
        try:
            self.sales_processor.convert_sales_column()
            test_obj.yakshaAssert("TestMissingColumn", False, "exceptional")
            print("TestMissingColumn = Failed")
        except ValueError as e:
            if str(e) == "'total_sales' column not found in the CSV file.":
                test_obj.yakshaAssert("TestMissingColumn", True, "exceptional")
                print("TestMissingColumn = Passed")
            else:
                test_obj.yakshaAssert("TestMissingColumn", False, "exceptional")
                print("TestMissingColumn = Failed")
