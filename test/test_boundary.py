import unittest
import numpy as np
from mainclass import SalesDataProcessor
from test.TestUtils import TestUtils
import pandas as pd


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.empty_file_path = 'empty_sales_data.csv'  # Empty file
        self.sales_processor = SalesDataProcessor(self.empty_file_path)

    def test_empty_csv(self):
        """Test handling of an empty CSV file."""
        test_obj = TestUtils()
        try:
            self.sales_processor.read_csv()  # This should raise an exception for empty data
            test_obj.yakshaAssert("TestEmptyCSV", False, "boundary")
            print("TestEmptyCSV = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyCSV", True, "boundary")
            print("TestEmptyCSV = Passed")

    def test_single_product_sales(self):
        """Test CSV with a single product entry."""
        # Mocking a DataFrame with a single row of data
        self.sales_processor.df = pd.DataFrame({
            'product_id': [1],
            'product_name': ['Product A'],
            'total_sales': [200.5],
            'units_sold': [10],
            'price': [20.05]
        })
        try:
            sales_array = self.sales_processor.convert_sales_column()
            expected_array = np.array([200.5])  # Expected result for the single entry
            test_obj = TestUtils()
            if np.array_equal(sales_array, expected_array):
                test_obj.yakshaAssert("TestSingleProductSales", True, "boundary")
                print("TestSingleProductSales = Passed")
            else:
                test_obj.yakshaAssert("TestSingleProductSales", False, "boundary")
                print("TestSingleProductSales = Failed")
        except Exception:
            test_obj.yakshaAssert("TestSingleProductSales", False, "boundary")
            print("TestSingleProductSales = Failed")
