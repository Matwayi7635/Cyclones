'''calculates uv winds against air temperature at 500 hPa level
   Adopted script from http://www.met.reading.ac.uk/~swsheaps/cf-plot-2.4.8/user_guide.html
'''
import cf
import matplotlib
matplotlib.use('pdf')#failure to include this results to an error
import matplotlib.pyplot as plt
import cfplot as cfp
f=cf.read('Geopotential.nc')#ggap.nc')
u=f[1].subspace(pressure=500)
v=f[2].subspace(pressure=500)
t=f[0].subspace(pressure=500)
cfp.gopen()
#cfp.mapset(lonmin=10, lonmax=120, latmin=-30, latmax=30)
cfp.mapset(lonmin=30, lonmax=70, latmin=-20, latmax=10)
cfp.levs(min=254, max=270, step=1)
cfp.con(t)
#cfp.plotvars.cs='#0000ff'
cfp.vect(u=u, v=v, key_length=10, scale=50, stride=2)
cfp.con(f=t, title='Zonal wind vs temperature')#,color='#00ff00')
#save figure
cfp.cscale('viridis', ncols=17)
cfp.plotvars.cs[14]='#d3d3d3'
plt.savefig('myfig2.pdf', dpi=1500)
cfp.setvars(file='zonalt.png', dpi=1000)
cfp.gclose()
#Set a box region with xpts & ypts
#xpts=[-30, 30, 30, -30, -30]
#ypts=[-8, -8, 5, 5, -8]
