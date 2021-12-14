# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:23:59 2021

@author: Aston
"""
import xarray as xr
f = xr.open_dataset('C:/NCL/era5.monthly.2018.GPI.nc')
print (f)
import numpy as np
import matplotlib.pyplot as plt
import cartopy as cart
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset

#f = Dataset('sst.mnmean.nc')
sst = f.variables['chi'][0,:,:]
lats = f.variables['lat'][:]
lons = f.variables['lon'][:]

ax = plt.axes(projection=cart.crs.PlateCarree())
ax.coastlines()
ax.add_feature(cart.feature.LAND, zorder=100, edgecolor='k')
ax.set_global()
plot = ax.contourf(lons, lats, sst, 60, transform=cart.crs.PlateCarree())
cb = plt.colorbar(plot)
plt.show()