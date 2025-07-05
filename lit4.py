#%%
import xarray as xr
import pandas as pd
from ecmwf.opendata import Client
import hvplot.xarray
import streamlit as st
from streamlit_bokeh import streamlit_bokeh
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

counties = gpd.read_file(r'https://gist.githubusercontent.com/sdwfrost/d1c73f91dd9d175998ed166eb216994a/raw/e89c35f308cee7e2e5a784e1d3afc5d449e9e4bb/counties.geojson')

#%%
x = hvplot.show(
    (euro['tp']*39.37).hvplot(height=600, width=1250, coastline=True, features={'states':'50m'})
)

st.bokeh_chart(x)