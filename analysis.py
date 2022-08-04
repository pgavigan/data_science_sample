# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:58:26 2022

@author: Patrick
"""

import matplotlib.pyplot as plt
import sqlite3 as sl
import pandas as pd


# Load the data from the database (or whatever other tool the data is stored in)
data = pd.read_sql("SELECT * FROM record", sl.connect('data.db'))

# Perform analysis. For the purpose of this example, plot some data...
# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()
