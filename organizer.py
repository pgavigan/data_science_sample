# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:46:00 2022

@author: Patrick

The role of this script is to take the RAW data files and put them into some 
sort of data warehouse (a database, AWS Redshift, or other)

"""


import sqlite3 as sl
import pandas as pd


def organizeData():
    
    # Load the raw data file(s)
    data = pd.read_json ('json_data.json')
    
   
    # Deal with loading it to a database (placeholder for something more sofisticated)
    databaseFileName = 'data.db'
    buildDatabase(databaseFileName)
    addRecords(databaseFileName, data)
    
    
    


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
        
    
def buildDatabase(dataBaseFileName):
    recordTable = ('''
                   create table if not exists record (
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       time REAL,
                       tavg REAL,
                       tmin REAL,
                       tmax REAL,
                       prcp REAL,
                       snow REAL,
                       wdir REAL,
                       wspd REAL,
                       wpgd REAL,
                       pres REAL,
                       tsun REAL);
                   ''') 
    dataBase = sl.connect(dataBaseFileName)
    runSQL(dataBaseFileName, recordTable)

    
def addRecords(fileName, records):
    con = sl.connect(fileName)
    try:
        sql = records.to_sql('record', con)
    except:
        pass    


    
if __name__ == '__main__':
    organizeData()
    
