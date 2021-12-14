import cfplot as cfp
from netCDF4 import Dataset as ncfile
nc = ncfile('cfplot_data/tas_A1.nc', 'r')#[0]
lons=nc.variables['lon'][:]
lats=nc.variables['lat'][:]
temp=nc.variables['tas'][0,:,:]
cfp.con(f=temp, x=lons, y=lats)