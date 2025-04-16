import unittest
import numpy as np
from mainclass import SalesDataProcessor
from test.TestUtils import TestUtils
import pandas as pd

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.file_path = 'sales_data.csv'  # Ensure this file exists or mock it in the tests
        self.sales_processor = SalesDataProcessor(self.file_path)

    def test_read_csv(self):
        """Test if CSV is read correctly."""
        try:
            self.sales_processor.read_csv()
            test_obj = TestUtils()
            test_obj.yakshaAssert("TestReadCSV", True, "functional")
            print("TestReadCSV = Passed")
        except Exception:
            test_obj.yakshaAssert("TestReadCSV", False, "functional")
            print("TestReadCSV = Failed")

    def test_convert_sales_column(self):
        """Test if the total_sales column is correctly converted to NumPy array."""
        try:
            self.sales_processor.read_csv()  # Read the CSV first
            sales_array = self.sales_processor.convert_sales_column()
            expected_array = np.array([200.5, 300.75, 400.0, 500.25])  # Replace with real expected values
            test_obj = TestUtils()
            if np.array_equal(sales_array, expected_array):
                test_obj.yakshaAssert("TestConvertSalesColumn", True, "functional")
                print("TestConvertSalesColumn = Passed")
            else:
                test_obj.yakshaAssert("TestConvertSalesColumn", False, "functional")
                print("TestConvertSalesColumn = Failed")
        except Exception:
            test_obj.yakshaAssert("TestConvertSalesColumn", False, "functional")
            print("TestConvertSalesColumn = Failed")
