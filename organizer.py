# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:46:00 2022

@author: Patrick

The role of this script is to take the RAW data files and put them into some 
sort of data warehouse (a database, AWS Redshift, or other)

"""


import sqlite3 as sl
import pandas as pd


# Load the raw data file(s)
data = pd.read_json ('json_data.json')
    
# Deal with loading it to a database (placeholder for something more sofisticated)
databaseFileName = 'data.db'
con = sl.connect(databaseFileName)
try:
    data.to_sql('record', con)
except:
    pass