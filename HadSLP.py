import cf
import cfplot as cfp
from netCDF4 import Dataset as ncfile
import matplotlib 
matplotlib.use('pdf')
import cartopy.crs as ccrs
#nc=cf.read('cfplot_data/tas_A1.nc')[0]
nc = ncfile('TC3_KEN-4.25.nc')#48_14.v4.nc')
lons=nc.variables['longitude'][:],
lats=nc.variables['latitude'][:]
temp=nc.variables['z'][3,:,:]
#temp=nc.subspace(time=cf.wi(cf.dt('1900-01-01'), cf.dt('1980-01-01')))
#cfp.levs(min=265, max=285, step=1)
#Labeling	plots	with	different	tick	marks	and	axis	labels #cfp.con(nc.collapse('mean','longitude'),\
#xticks=xticks,xticklabels=xticklabels,yticks=yticks,yticklabels=yticklabels,xlabel='x-axis',ylabel='y-axis')
#*********************
#
cfp.levs(extend='min')# manual=[-10, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 10])
cfp.con(f=temp,xlabel='Longitude',ylabel='Latitude',\
 ptype=3, colorbar_orientation='horizontal', negative_linestyle='dashed', colorbar_title='Air temperature $^oC$', colorbar_drawedges=True, title='Air Mean 1979-2005')

#cfp.con(f=temp,xlabel='Longitude',ylabel='Latitude',\
#colorbar_orientation='horizontal', negative_linestyle='dashed', colorbar_title='Air temperature $^oC$', colorbar_drawedges=True, title='Air Mean 1979-2005')
# A box location inside a map
#cfp.plotvars.mymap.plot([-170, -170, -120, -120, -150],
#                        [-5, 5, 5, -5, -5], linewidth=2.0, color='red')#,transform=ccrs.PlateCarree)#cfp.con(f=temp, x=lons, y=lats, ptype=1,colorbar_orientation='horizontal', title='Masked data plotted in grey')
cfp.setvars(file='z.pdf', land_color= False)
#cfp.setvars(file='HadSLPm.png', land_color= False)
cfp.gclose()
#g=f.collapse('area:	mean',	weights='area')	#	Area	mean	for	each	time 
#g=g.collapse('T:	max')	#	Time	maxiumum	of	the	area	means 
#ptype=1