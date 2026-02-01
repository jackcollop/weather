#%%
import xarray as xr
import pandas as pd
from ecmwf.opendata import Client
import hvplot.xarray
import streamlit as st
from streamlit_bokeh import streamlit_bokeh
from bokeh.plotting import figure

#%%

client = Client("ecmwf", beta=False)
parameters = ['tp']
filename = 'medium-rain-acc.grib'
filename
#%%

client.retrieve(
    step=240,
    stream="oper",
    type="fc",
    levtype="sfc",
    resol='0p25',
    param=parameters,
    target=filename
)


#%%
euro = xr.open_dataset(filename, engine='cfgrib')
#%%

#%%
x =  (euro['tp']*39.37).hvplot(height=600, width=1250, coastline=True, features={'states':'50m'})


streamlit_bokeh(hvplot.render(x))




