#%%
import xarray as xr
import pandas as pd
from ecmwf.opendata import Client
import hvplot.xarray
import streamlit as st
from streamlit_bokeh import streamlit_bokeh
from bokeh.plotting import figure
import geopandas as gpd

#%%

client = Client("ecmwf", beta=False)
parameters = ['tp']
filename = 'medium-rain-acc.grib'
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

df = pd.read_csv(r'C:\Users\john.collop\Downloads\acres.csv')
#%%
df.set_index(df.ANSI.astype(str), inplace=True)
#%%
import geopandas as gpd
import geoviews as gv

counties = gpd.read_file(r'https://gist.githubusercontent.com/sdwfrost/d1c73f91dd9d175998ed166eb216994a/raw/e89c35f308cee7e2e5a784e1d3afc5d449e9e4bb/counties.geojson')

counties.set_index(counties.GEOID.astype(str), inplace=True)
#%%
counties = counties.join(df)
#%%
counties.dropna(inplace=True)

#%%
euro = xr.open_dataset(filename, engine='cfgrib')
#%%

#%%
x =  (euro['tp']*39.37).hvplot(coastline=True, features={'states':'50m'}) * gv.Polygons(counties[['LOCATION_DESC','VALUE','geometry']]).opts(color='VALUE',alpha=0.25, cmap='kgy')


streamlit_bokeh(hvplot.render(x), use_container_width=True)











