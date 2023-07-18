### -ACCENTURE CONFIDENTIAL-
### Type: Source Code
###
### Copyright (c) 2023, ACCENTURE
### All Rights Reserved.
###
### This unpublished material is proprietary to ACCENTURE. The methods and
### techniques described herein are considered trade secrets and/or
### confidential. Reproduction or distribution, in whole or in part, is
### forbidden except by express written permission of ACCENTURE.

import unittest
import pandas as pd
from app.utils.lib import *


# Define a test class for your module
class TestLibModule(unittest.TestCase):

    # Test api_response_to_dataframe function
    def test_api_response_to_dataframe(self):
        data = {'totalSize': 0}
        result = api_response_to_dataframe(data)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(result.columns[0], 'A')

    # Test read_dataframe_from_csv function
    def test_read_dataframe_from_csv(self):
        # Test when the file is found
        df = read_dataframe_from_csv('test_data.csv')
        self.assertIsInstance(df, pd.DataFrame)

        # Test when the file is not found
        df = read_dataframe_from_csv('non_existent_file.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 0)

    # # Test execute_soql_query function
    # def test_execute_soql_query(self):
    #     # Mock your Salesforce object or use a test environment to test this function
    #     # You can also use the mock library to create a mock Salesforce object

    #     # Sample test case with a mock Salesforce object
    #     sf = MockSalesforceObject()
    #     query = "SELECT Id, Name FROM Account LIMIT 5"
    #     keys = {'key1', 'key2'}
    #     result = execute_soql_query(sf, query, keys)
    #     self.assertIsInstance(result, dict)

    # Test filter_record function
    def test_filter_record(self):
        row = pd.Series({'Id': '123', 'Name': 'John', 'Age': 30})
        filtered_record = filter_record(row)
        self.assertIsInstance(filtered_record, dict)
        self.assertNotIn('Id', filtered_record)
        self.assertIn('Name', filtered_record)
        self.assertIn('Age', filtered_record)

    # Test vlookup_id function
    def test_vlookup_id(self):
        # Define test DataFrames with sample data
        df_current = pd.DataFrame({'Id': ['123', '456'], 'Name': ['John', 'Alice']})
        df_lookup = pd.DataFrame({'Id': ['123', '456'], 'new_Id': ['987', '654']})
        current_record_id_column = 'Id'

        result = vlookup_id(df_current, df_lookup, current_record_id_column)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.loc[0, current_record_id_column], '987')
        self.assertEqual(result.loc[1, current_record_id_column], '654')


if __name__ == '__main__':
    unittest.main()
