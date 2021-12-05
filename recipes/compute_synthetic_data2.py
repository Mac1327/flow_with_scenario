# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from scipy import stats
import datetime

n_days =365*5
unit_cost = 3.5

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
def make_auto_ts(ar1=0.99,ar2=0, n=n_days, y0 = 0, y1 = 0, mu=0, sigma=1, cust= 50,days_empty = 7):

    X=np.arange(n)
    y_list = []
    for i in range(n):
        # build an AR process of params (beta_1, beta_2) = (ar1, ar2)
        # With noise epsilon(t) = Normal(mu, sigma)
        y_new = np.round(ar1 * y1 + ar2* y0 + stats.norm.rvs(mu,sigma))
        y0 = y1
        y1 = y_new.copy()
        y_list.append(y0)
    y_list = np.array(y_list) + cust
    no_sales = np.random.choice(range(len(y_list)),10, replace=False)
    for n in no_sales:
        y_list[n:n+days_empty] =  0
    return y_list

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
n_products = 5

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(n_days)]
df = pd.DataFrame()
df["date_time"] = date_list
for product in range(n_products):
    cust = np.random.randint(45,65)
    y_list =  make_auto_ts(cust= cust)
    df[f"units_0{product+1}"] = y_list

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_long= pd.wide_to_long(df, stubnames="units_", i="date_time", j="prod", sep='', suffix='\\d+').sort_values("date_time")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_long.reset_index(inplace=True)


# Write recipe outputs
synthetic_data2 = dataiku.Dataset("synthetic_data2")
synthetic_data2.write_with_schema(df_long)
