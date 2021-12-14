import cf
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import cfplot as cfp
#f=cf.read('cfplot_data/ggap.nc')[0]
f=cf.read('slp.mnmean.real.nc')#[0]
#latitude - pressure - zonal mean-1
#cfp.con(f.collapse('mean','longitude'),title='Pressure zonal mean')

#Latitude Pressure-2
cfp.con(f.subspace(longitude=0),title='Latitude pressure')

#latitude - log pressure-0
#cfp.con(f.collapse('mean','longitude'), ylog=True,title='latitude - log pressure')

#Longitude pressure-0
#cfp.con(f.collapse('mean', 'latitude'), title='Longitude pressure')

plt.savefig('hadslp.png')
cfp.setvars(file='hadslp.pdf')
cfp.gclose()