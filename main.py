#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 2023

@author: corey
"""

# Corey Yang-Smith
# May 10  2023
# First Round at this data, hoping to make some business solutions
# Want to understand the business better and get more comfortable generating a variety of charts.
# Bonus: Create a regression model predicting sales
#
# Dataset
# https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
#
# Weekly Project #1
#
#
################################################################################################################################

#Import Libraries
import geopandas as gpd
import pandas as pd

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

import folium
from folium.features import GeoJsonTooltip

file_name = "superstore-utc8.csv"
df = pd.read_csv(file_name)

print("")
print("Head")
print("")
print(df.head())

print("")
print("Datatypes")
print("")
print(df.dtypes)

####################################
#### CHART 1 | Region Intensity ####
####################################
# Folium circle heat map indicating the largest buyers

############################################
#### CHART 2 | Segment Splits by Region ####
############################################
# Stacked bar chart?
# It will be by freqency
# by sale
# by profit
#

####################################################
#### CHART 3 | Total Sales & Profit by Category ####
####################################################
sales_by_cateogory = df.groupby(['Category'])['Sales'].sum()
print("")
print("SALES BY CATEGORY")
print("")
print(sales_by_cateogory.head())
print("")
sales_by_cateogory.plot(kind='barh')
plt.title("Sales by Category for Superstore")
plt.xlabel("Sales")
plt.ylabel("Categories")
plt.show()

profit_by_category = df.groupby(['Category'])['Profit'].sum()
print("")
print("PROFIT BY CATEGORY")
print("")
print(profit_by_category.head())
print("")
profit_by_category.plot(kind='barh')
plt.title("Profit by Category for Superstore")
plt.xlabel("Profit")
plt.ylabel("Categories")
plt.show()


#################################################
#### CHART 4 | Total Sales & Profit by State ####
#################################################

sales_by_state = df.groupby(['State'])['Sales'].sum()
print("")
print("SALES BY STATE")
print("")
print(sales_by_state.head())
sales_by_state.plot(kind='barh')
print("")
plt.title("Sales by State for Superstore")
plt.xlabel("Sales")
plt.ylabel("States")
plt.show()

profit_by_state = df.groupby(['State'])['Profit'].sum()
print("")
print("PROFIT BY STATE")
print("")
print(profit_by_state.head())
print("")
profit_by_state.plot(kind='barh')
plt.title("Profit by State for Superstore")
plt.xlabel("Profit")
plt.ylabel("States")
plt.show()

##################################################
#### CHART 5 | Total Sales & Profit by Region ####
##################################################

sales_by_region = df.groupby(['Region'])['Sales'].sum()
print("")
print("SALES BY REGION")
print("")
print(sales_by_region.head())
sales_by_region.plot(kind='barh')
print("")
plt.title("Sales by Region for Superstore")
plt.xlabel("Sales")
plt.ylabel("Regions")
plt.show()

profit_by_region = df.groupby(['Region'])['Profit'].sum()
print("")
print("PROFIT BY REGION")
print("")
print(profit_by_region.head())
print("")
profit_by_region.plot(kind='barh')
plt.title("Profit by Region for Superstore")
plt.xlabel("Profit")
plt.ylabel("Regions")
plt.show()

#########################################################
#### CHART 6 | Average Purchase Quantity - Histogram ####
#########################################################
# Have to fix using num pay buckets or other method?
# TODO
avg_purchase_qty_hist = df.groupby(['Quantity']).sum()
print("")
print("AVERAGE PURHCASE QUANTITY")
print("")
print(avg_purchase_qty_hist.head())
avg_purchase_qty_hist.plot(kind='hist')
print("")
plt.title("Average Purchase Quantity")
plt.xlabel("Sales")
plt.ylabel("Regions")
plt.show()

print("###########################")
print("Code Successfully Executed!")
print("###########################")