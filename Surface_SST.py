import matplotlib.pyplot as plt
import xarray as xr
import numpy as np

import IPython.display
import cmocean as cm
import cartopy.crs as ccrs
import cosima_cookbook as cc
session = cc.database.create_session()
expt = 'ersst.mnmean.v5.nc'
variable = 'sst'
darray = cc.querying.getvar(expt, variable, session, frequency='1 monthly', n=-1)
#SST = darray.mean('time') - 273.15; # convert from degrees K to degrees C
plt.figure(figsize=(8, 4))
ax = plt.axes(projection=ccrs.Robinson())
SST.plot.pcolormesh(ax=ax, transform=ccrs.PlateCarree(), x='xt_ocean', y='yt_ocean', cmap=cm.cm.thermal, vmin=-2, vmax=30)
ax.coastlines()