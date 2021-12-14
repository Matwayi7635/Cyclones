#import xarray as xr
#ds = xr.open_dataset('fnl_20190301_00_00.grib2', engine='cfgrib')
#ds

import cfgrib
cfgrib.open_datasets('fnl_20190301_00_00.grib2')