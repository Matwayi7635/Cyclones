#-- Draw anomalies for 1997 and 1998
#%matplotlib inline
import os
import pandas as pd
from netCDF4 import  num2date
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

import cf
import cfplot as cfp
from netCDF4 import Dataset as ncfile
f2 = ncfile('output_freq.nc.nc')#[1]

anom = f2.variables["freq"] #read anomaly from previous resuts
time = f2.variables["time"] #read time
dlons = f2.variables["lon"][:] # read longitudes
dlats = f2.variables["lat"][:] # read latitudes

ndate = num2date(time[:],units=time.units,calendar=time.calendar) #convert time to date
#dates = pd.DatetimeIndex(ndate) # convert date to date object in pandas

syear=1997 # start of plot
eyear=1998 # end of plot

fig = plt.figure(figsize=(24,24)) # set figure environemnt

contours=np.arange(-4.0,4.0,0.5) # set contours
cmap=cm.bwr # set colormap

############

# set up label
cax = fig.add_axes([0.2, -0.050, 0.6, 0.03]) 
#art = plt.colorbar(cs, cax, orientation='horizontal')
#set_label('SST Anomaly [K]', fontsize=20)
#ax.tick_params(labelsize=18)

# adjust layout
#plt.tight_layout(pad=0.2, w_pad=0.2, h_pad=0.3)

# show
plt.show()