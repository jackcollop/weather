import pandas as pd
import streamlit as st
import pydeck as pdk
import xarray as xr
import streamlit_bokeh
from ecmwf.opendata import Client
import hvplot.xarray

client = Client("ecmwf", beta=False)
parameters = ['tp']
filename = 'medium-rain-acc.grib'
filename

client.retrieve(
    step=240,
    stream="oper",
    type="fc",
    levtype="sfc",
    resol='0p25',
    param=parameters,
    target=filename
)


euro = xr.open_dataset(filename, engine='cfgrib')

streamlit_bokeh.streamlit_bokeh(hvplot.show((euro['tp']*39.37).hvplot(height=600, width=1250, coastline=True, features={'states':'50m'})))
