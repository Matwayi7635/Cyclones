import cf
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import cfplot as cfp
#f=cf.read('cfplot_data/tas_A1.nc')[0]
f=cf.read('Wind.hgt.STDANOM.nc')[0]#cfplot_data/ggap.nc')[0]#ggap.nc/tas_A1.nc
#u=f.subspace(time=cf.Y(10))[0]

#u = f.subspace(time=15)
#u = f.subspace[15, 'longitude', 'latitude']
print(f) 
#u=f.collapse('eastward_wind')[0]
#u_mean=u.collapse('mean', 'longitude')
#cfp.con(f=u, ylog=True)
# Make a zonal mean zonal wind plot
#cfp.con(u_mean)
# Make a log y-axis plot of the zonal mean zonal wind
#cfp.con(latitude, ylog=True)
#cfp.con (f.collapse('mean',	'latitude'))
#cfp.con(f.collapse('f','longitude'), ylog=True)
cfp.con(cf.collapse(f, 'mean','longitude'), ylog=1)
plt.savefig('myfig13.pdf')
cfp.gclose()