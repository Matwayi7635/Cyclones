import cf
import cfplot as cfp
from netCDF4 import Dataset as ncfile
import matplotlib 
matplotlib.use('pdf')
import cartopy.crs as ccrs
#nc=cf.read('cfplot_data/tas_A1.nc')[0]
nc = ncfile('ersst7905SON.nc')#48_14.v4.nc')
lons=nc.variables['lon'][:]
lats=nc.variables['lat'][:]
temp=nc.variables['sst'][0,:,:]
#temp=nc.subspace(time=cf.wi(cf.dt('1900-01-01'), cf.dt('1980-01-01')))
#cfp.levs(min=265, max=285, step=1)
#Labeling	plots	with	different	tick	marks	and	axis	labels #cfp.con(nc.collapse('mean','longitude'),\
#xticks=xticks,xticklabels=xticklabels,yticks=yticks,yticklabels=yticklabels,xlabel='x-axis',ylabel='y-axis')
cfp.con(f=temp,xlabel='Longitude',ylabel='Latitude',\
x=lons, y=lats, ptype=1,colorbar_orientation='horizontal', negative_linestyle='dashed', colorbar_title='Air temperature $^o C$', colorbar_drawedges=True, title='ERSST SON Anomalies 1979-2005')
# A box location inside a map
#cfp.plotvars.mymap.plot([-170, -170, -120, -120, -150],
#                        [-5, 5, 5, -5, -5], linewidth=2.0, color='red')#,transform=ccrs.PlateCarree)#cfp.con(f=temp, x=lons, y=lats, ptype=1,colorbar_orientation='horizontal', title='Masked data plotted in grey')
cfp.setvars(file='ersst7905SON.pdf', land_color= True)
cfp.gclose()
#g=f.collapse('area:	mean',	weights='area')	#	Area	mean	for	each	time 
#g=g.collapse('T:	max')	#	Time	maxiumum	of	the	area	means 