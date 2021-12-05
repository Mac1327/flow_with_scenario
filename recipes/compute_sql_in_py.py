# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from dataiku import SQLExecutor2, Dataset
from dataikuapi import DSSClient

client = dataiku.api_client()
project_key = dataiku.get_custom_variables()['projectKey']
executor = SQLExecutor2(connection="test_connection")

# Read recipe inputs
synthetic_data2_prepared = dataiku.Dataset("synthetic_data2_prepared")
synthetic_data2_prepared_df = synthetic_data2_prepared.get_dataframe()

which_query = int(dataiku.get_custom_variables()['which_query'])

if which_query == 1:
    query = f"""SELECT *
                FROM "{project_key}_synthetic_data2_prepared"
                LIMIT(1) """
elif which_query == 2:
    query = f"""SELECT * 
                FROM "{project_key}_synthetic_data2_prepared" 
                LIMIT(100) """

sql_in_py_df = executor.query_to_df(query)

# Write recipe outputs
sql_in_py = dataiku.Dataset("sql_in_py")
sql_in_py.write_with_schema(sql_in_py_df)