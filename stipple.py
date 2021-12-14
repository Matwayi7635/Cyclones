import cf, cfplot as cfp
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
f=cf.read('cfplot_data/tas_A1.nc')[0]
g=f.subspace(time=15)
cfp.gopen()
cfp.cscale('magma')
cfp.mapset(proj='spstere')
cfp.con(g)
cfp.stipple(f=g, min=265, max=295, size=100, color='#8A2BE2')
#cfp.TITLE='Jan 1987 - 100mb Geopotential Height'
cfp.con(f=g, title='South Polar Plot')
#cfp.con(f=g, CB_TITLE='ms!E-1!N')
#plt.savefig('stiple.pdf')
cfp.setvars(file='zonalS.png')
cfp.gclose()
