#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning

# ## Overview

import pandas as pd
sales = pd.read_excel("./data/Capstone Project Data Extract - Sales.xlsx", header=2)
traffic = pd.read_excel("./data/Capstone Project Data Extract - Traffic.xlsx", header=2)

sales.info()
sales.head(5)
sales.describe()


# *Remark*
# - No missing values
# - Negative `sales unit` and `sales retail` (refund/store adjustment)

traffic.info()
traffic.head(5)
traffic.describe()


# ## Renaming columns

sales.rename(columns={"Unnamed: 1": "store name", 
                      "Unnamed: 3": "group name",
                      "Unnamed: 6": "month end",
                      "SLS UNT": "sales unit",
                      "SLS RTL": "sales retail"},
             inplace=True)

sales.columns = map(str.lower, sales.columns)
sales.head(5)
traffic.rename(columns={"Unnamed: 1": "store name",
                        "Unnamed: 4": "month end"},
               inplace=True)
traffic.columns = map(str.lower, traffic.columns)
traffic.head(5)


# ## Cleaning data types
sales.info()
sales.date = pd.to_datetime(sales.date, format='%b-%d-%Y')
sales.date.head(5)

traffic.info()
traffic.date = pd.to_datetime(traffic.date, format='%b-%d-%Y')
traffic.date.head(5)


# ## Merging tables
assert sales.store.unique().all() == traffic.store.unique().all()
assert sales.date.nunique() == traffic.date.nunique()
set(traffic.date.unique()) - set(sales.date.unique())
traffic[traffic.date == '2019-08-29']


# **Remark:** Mismatch between sales/traffic data. Sales is missing data for 2019-08-29.
# For consistency, we will retain records until 2019-08-28 (using inner join by default in Python).

df = pd.merge(sales, traffic, 
              on=['store', 'store name', 'year', 'month','month end', 'week', 'date'])
df.head(5)

