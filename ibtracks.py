# -*- coding: utf-8 -*-
import numpy as np
# functions for working with dates
import datetime
# needed for reading data
import netCDF4 as nc
from netCDF4 import Dataset
# used for creating plots
import matplotlib.pyplot as plt
import seaborn as sns
# for smoothing the visualization of the TUTT
from statsmodels.nonparametric.smoothers_lowess import lowess
# mapping tools are in cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# plot parameters
sns.set_style('white')
xfr = LongitudeFormatter(zero_direction_label=True)
yfr = LatitudeFormatter()

# directories
ddir = '../data/'
fdir = '../figs/'

# function to return month given modified Julian day
def mjd2month(mjd,y0=1858,m0=11,d0=17):
    """
    A function for finding the month of a date expressed in
    days relative to some baseline date (can be modified to
    get other aspects of the date as well)

    Variables:
    mjd    :: relative date (scalar)
     (note: arrays will not work for mjd under this approach)

    Parameters:
    y0     :: year of baseline date
    m0     :: month of baseline date
    d0     :: day of baseline date

    Note:
    The default date used in this function corresponds to
    the modified Julian date used by the IBTrACS data set.
    """
    date0 = datetime.datetime(year=y0, month=m0, day=d0)
    date1 = date0 + datetime.timedelta(days=mjd)
    return date1.month

# read in IBTraCS data (center 10 is JTWC - WP)
ncdf = nc.Dataset(ddir+'IBTrACS.SI.v04r00.nc')
#year = ncdf.variables['season'][:]           # year
##genb = ncdf.variables['genesis_basin'][:]    # 2 = Western North Pacific
#tc_v = ncdf.variables['source_wind'][:,:,10] # wind speed, in knots
#tc_y = ncdf.variables['source_lat'][:,:,10]  # latitude of storm center
#tc_x = ncdf.variables['source_lon'][:,:,10]  # longitude of storm center
#tc_t = ncdf.variables['source_time'][:,:]    # modified Julian day (6-hourly)
#ttyp = ncdf.variables['track_type'][:]       # 0,1 include cyclogenesis
#print (ncdf.variables.keys())
print (ncdf.dimensions.keys())
#ncdf.close()