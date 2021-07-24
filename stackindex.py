from kats.consts import TimeSeriesData
from kats.models.prophet import ProphetModel, ProphetParams
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


#read the csv file
df = pd.read_csv("stackindex.csv")

# Turn the month column into datetime
df["month"] = pd.to_datetime(df["month"], format="%y-%b")

#set month as index
df = df.set_index("month")

def getdata(inputcol):
    input_col =  input("Enter name : ")
    

