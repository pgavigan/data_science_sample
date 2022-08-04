# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:58:26 2022

@author: Patrick
"""

import matplotlib.pyplot as plt


# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()



def runSQL(fileName, sql, values = None):
    dataBase = sl.connect(fileName)
    with dataBase:
        if values == None:
            result = dataBase.execute(sql)
        elif isinstance(values, list):
            result = dataBase.executemany(sql,values)
        else:
            result = dataBase.execute(sql,values)
    result = result.fetchall()
    dataBase.close()
    return result

def getRecords():
    sql = "SELECT * FROM record"
    records = []
    for record in records:
        values = (start.timestamp(), stop.timestamp(), fileName)
        records.extend(runSQL(sql, values))
    return records
  