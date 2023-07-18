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


import pandas as pd
import numpy as np
import logging
from simple_salesforce import format_soql
import inspect
import logging
import functools
import time


def log_function_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f"Started execution of {func.__name__}")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        logging.debug(f"Finished execution of {func.__name__} "+
                     f"in {end_time - start_time:.4f} seconds")
        return result

    return wrapper

@log_function_execution
def api_response_to_dataframe(data):
    """
    Converts the API response from simple_salesforce into a pandas DataFrame.

    Parameters:
        data (dict): The response from a query made using simple_salesforce.

    Returns:
        DataFrame: A table representing the query result.
            If no records are found, None is returned.
    """

    if data['totalSize'] == 0:
        return pd.DataFrame(columns=['A'])
    
    df = pd.DataFrame(data['records']).drop('attributes', axis=1)

    list_columns = list(df.columns)
    for col in list_columns:
        if any(isinstance(df[col].values[i], dict)
               for i in range(0, len(df[col].values))):
            df = pd.concat(
                [
                    df.drop(columns=[col]),
                    df[col].apply(pd.Series)
                    .drop('attributes', axis=1).add_prefix(col + '.')
                ],
                axis=1)
            new_columns = np.setdiff1d(df.columns, list_columns)
            for i in new_columns:
                list_columns.append(i)
    
    return df

@log_function_execution
def read_dataframe_from_csv(filename):
    """
    Reads a DataFrame from a CSV file.

    Parameters:
        filename (str): The name of the CSV file to read.

    Returns:
        DataFrame: The contents of the CSV file as a DataFrame.
            Returns an empty DataFrame if the file is not found.
    """
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError as e:
        logging.warning(f"File '{filename}' not found. "
                        "There may be no records to insert.")
        logging.error(e)
        df = pd.DataFrame()

    # Replace any NaN values with empty strings if present
    df = df.fillna('')  
    return df

@log_function_execution
def execute_soql_query(sf, query, keys):
    """
    Executes an SOQL query, handles exceptions, and provides logs.

    Args:
        sf (Salesforce object): An instance of the Salesforce organization.
        query (str): The raw SOQL query.
        keys (set of str): Set of email keys.

    Returns:
        dict: The response of the SOQL query in JSON format.
    """
    formatted_query = format_soql(query, keys=list(keys))
    logging.debug('Executing query: \n' + formatted_query)

    response = sf.query_all(formatted_query)
    logging.debug('Query execution success')
    return response

import logging


@log_function_execution
def filter_record(row):
    """
    Filter the given row and return a dictionary containing only the valid
    key-value pairs.

    This function filters out key-value pairs in the input row where:
    - The key contains a dot ('.') character,
    - The key is equal to 'Id', or
    - The key is equal to 'new_Id'.

    Parameters:
        row (pandas.Series): The input row as a pandas Series.

    Returns:
        dict: A dictionary containing valid key-value pairs from the input row.
    """
    valid_keys = filter(
        lambda key_value: 
            '.' not in key_value[0] and key_value[0] not in ('Id', 'new_Id'),
        row.to_dict().items()
    )
    filtered_record = dict(valid_keys)
    return filtered_record

@log_function_execution
def vlookup_id(df_current, df_lookup, current_record_id_column):
    """
    Perform a VLOOKUP-like operation to map IDs in df_current to corresponding new IDs from df_lookup.

    This function iterates through the rows of df_current, looks up the corresponding record in df_lookup based
    on the provided current_record_id_column, and replaces the current IDs with the corresponding new IDs.

    Parameters:
        df_current (pandas.DataFrame): The DataFrame containing the current records with IDs to be mapped.
        df_lookup (pandas.DataFrame): The DataFrame containing the mapping of old IDs to new IDs.
        current_record_id_column (str): The name of the column in df_current that contains the current IDs.

    Returns:
        pandas.DataFrame: A new DataFrame with the current IDs replaced by their corresponding new IDs.
    """
    for index, row in df_current.iterrows():
        current_id = row[current_record_id_column]
        object_record = df_lookup[df_lookup['Id'] == current_id]
        new_object_id = ''

        if len(object_record) == 1:
            for new_id in object_record['new_Id']:
                new_object_id = new_id
        else:
            ## need to handle multiple matches or no matches
            pass

        df_current.at[index, current_record_id_column] = new_object_id

    return df_current







