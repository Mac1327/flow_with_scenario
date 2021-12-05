# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
synthetic_data2_prepared = dataiku.Dataset("synthetic_data2_prepared")
synthetic_data2_prepared_df = synthetic_data2_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

sql_in_py_df = synthetic_data2_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
sql_in_py = dataiku.Dataset("sql_in_py")
sql_in_py.write_with_schema(sql_in_py_df)
