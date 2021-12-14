#!/usr/bin/env python
# Wenchang Yang (wenchang@princeton.edu)
# Wed Jun 10 14:52:28 EDT 2020
if __name__ == '__main__':
    from misc.timer import Timer
    tt = Timer(f'start {__file__}')
import sys, os.path, os, glob
import xarray as xr, numpy as np, pandas as pd
#import matplotlib.pyplot as plt
#more imports
from xtc import tc_density
#
if __name__ == '__main__':
    tt.check('end import')
#
#start from here
savedfile = os.path.abspath(__file__).replace('.py', '.nc')
dataname = 'gdensity'
long_name = 'TC genesis density'

if os.path.exists(savedfile): # read from saved file
    print('**reading from saved file**:', savedfile)
    with xr.open_dataset(savedfile) as ds:
        da = ds[dataname]
else: # calculate from raw tracks data
    #ifile = '/tigress/wenchang/analysis/TC/HIRAM/amipHadISST_tigercpu_intelmpi_18_540PE/netcdf/tc_tracks.TS.1971-2018.nc'
    #ifile = '/tigress/wenchang/analysis/TC/ERA5/exp_p75C_550k_48h_12ms/netcdf/tc_tracks.1979-2018.nc'
    ifile = '/tigress/wenchang/data/ibtracs/v04r00/analysis/v2/IBTrACS.ALL.v04r00.tracksByYear.1980-2019.nc'
    with xr.open_dataset(ifile) as ds:
        #ds['windmax'] = ds['vmax']
        #da = tc_density(ds, lowpass_on=True, genesis_on=True, genesis_condition=(ds.windmax>17)&(ds.tm>0))
        ds['lon'] = ds['lon'].where(ds['lon']>0, other=ds['lon']+360)
        da = tc_density(ds, lowpass_on=True, genesis_on=True, genesis_condition=(ds.windmax>17))
        da = da.assign_attrs(long_name=long_name)
        da.to_dataset(name=dataname).to_netcdf(savedfile)
        print('**saved**:', savedfile)

 
 
if __name__ == '__main__':
    from wyconfig import * #my plot settings
    from geoplots import mapplot
    fig, ax = plt.subplots()
    years = slice('1980', '2018')
    figname = __file__.replace('.py', f'.aclim{years.start}-{years.stop}.{tt.today()}.png')
    da.sel(time=years).groupby('time.year').sum('time').mean('year') \
        .assign_attrs(long_name=da.attrs['long_name'], units=da.attrs['units'].replace('month', 'year'))\
        .plot.contourf(cmap='OrRd', levels=2.**np.arange(-2, 3.1, 0.5), cbar_kwargs=dict(aspect=30))
    mapplot()
    ax.set_title(f'IBTrACS {years.start}-{years.stop} TC genesis density')

    plt.savefig(figname)
    print('**saved**:', figname)

    tt.check(f'**Done**')
    plt.show()
    
