# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:40:08 2022

@author: Patrick

This script is modified from: https://meteostat.net/en/blog/obtain-weather-data-any-location-python

The role of this script is to go out to the internet (or wherever) and get RAW 
data. This RAW data is saved to some sort of storage container. Although this 
example downloads data for a set date range (which does not change) it is 
anticipated that a script of this type would need to run periodically to get 
new/ updated data.

"""

# Import Meteostat library and dependencies
from datetime import datetime
from meteostat import Point, Daily

# Set time period - imagine that this could run daily (or otherwise) for different date ranges
start = datetime(2018, 1, 1)
end = datetime(2018, 12, 31)

# Create Point for Vancouver, BC
vancouver = Point(49.2497, -123.1193, 70)

# Get daily data for 2018
data = Daily(vancouver, start, end)
data = data.fetch()


'''
For the purposes of this example it will save the data to a JSON file. 
Another script will read that file and put the data in a database.
Naturally, this step could be skipped and the data could be put straight in 
a database (this data is pretty simple), but other types of data may not be 
easily put in a database without some other preprocessing first, so I want to 
leave a placeholder for that step.
'''

data.to_json(path_or_buf = 'json_data.json')
