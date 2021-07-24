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

def plotdata(input_col):
    for column in df:
        if input_col == column:
            new_frame = df[column].to_frame()
            train_len = 102
            train = new_frame.iloc[:train_len]
            test = new_frame.iloc[train_len:]
            ts = TimeSeriesData(train.reset_index(), time_col_name="month")

            # Specify parameters
            params = ProphetParams(seasonality_mode="multiplicative")

            # Create a model instance
            m = ProphetModel(ts, params)

            # Fit mode
            m.fit()

            # Forecast
            fcst = m.predict(steps=50, freq="MS")
  
    

            m.plot()
            plt.savefig('static/figure1.png')
            return None
    
    

