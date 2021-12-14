from netCDF4 import Dataset
import scipy.interpolate
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

nc_f = 'TC3_KEN-4.25.nc'  
nc_fid = Dataset(nc_f, 'r')

lats = nc_fid.variables['latitude']  
lons = nc_fid.variables['longitude']

time = nc_fid.variables['time']
hgt = nc_fid.variables['z']#[3,:]

m = Basemap(width=5000000,height=3500000,
 resolution='l',projection='stere', lat_0 = 60, lon_0 = 70, lat_ts = 40)

m.drawcoastlines()
m.drawcountries()
lons, lats = np.meshgrid(lons, lats)
x, y = m(lons, lats)

# plot the first ZZ of hgt500
clevs = np.arange(400.,604.,4.)
cs = m.contour(x, y, hgt[0] * .1, clevs, linewidths=1.5, colors = 'k')
plt.clabel(cs, inline=1, fontsize=15, color='k', fmt='%.0f') 

# color grid
pcl = m.pcolor(x,y,np.squeeze(hgt[0]*.1))
cbar = m.colorbar(pcl, location='bottom', pad="10%")
cbar.set_label("hPa")

plt.title('500 hPa Geopotential Height')
plt.show() 