# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:04:36 2020

@author: alyss
"""

import pandas as pd

location = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_time_series/time_series_19-covid-Confirmed_archived_0325.csv'
df = pd.read_csv(location, error_bad_lines=False)

df2 = df.iloc[:,1:]
df2 = df2.drop(['Lat','Long'], axis = 1)
df3 = df2.groupby('Country/Region').sum()

df4 = df3.agg(['sum']).T


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
print (__version__)


import plotly.graph_objs as go

plot([go.Scatter(x=df4.index, y=df4['sum'])])
'file:///home/nbuser/library/temp-plot.html'

