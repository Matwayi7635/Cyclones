import cf, cfplot as cfp
import cf, cfplot as cfp
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
f=cf.read('cfplot_data/tas_A1.nc')[0]
cfp.gset(-30, 30, '1960-1-1', '1980-1-1')
cfp.levs(min=280, max=305, step=1)
cfp.cscale('plasma')
cfp.con(f.subspace(longitude=0), lines=0, title='Hovmuller')
#cfp.con(f=g, title='Polar plot with regular point')
plt.savefig('hov.pdf')
cfp.setvars(file='hov.png')
cfp.gclose()