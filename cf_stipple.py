import cf
import matplotlib
import cfplot as cfp
matplotlib.use('pdf')
f=cf.read('SLP_Aprildetrend.nc')[0] #cfplot_data/tas_A1.nc
g=f.subspace(time=15)
#g=f.subspace(time=cf.mam()
#g=[cf.year(cf.wi(1981, 1990)
#g = f.subspace(cf.wi(1976,1980))
#g = f.subspace(time='over_years')
cfp.gopen()
cfp.mapset(proj='spstere')
cfp.cscale('magma')
cfp.con(g)
#cfp.con(f.subspace(time=15), title='top')
cfp.stipple(f=g, min=220, max=260, size=100, color='#00ff00')
cfp.stipple(f=g, min=300, max=330, size=50, color='#0000ff', marker='s')
#cfp.stipple(f=g, min=265, max=295, size=100, color='#00ff00')
#cfp.stipple(f=g, min=300, max=330, size=50, color='#0000ff', marker='s')
cfp.setvars(file='stipplemamS.pdf')
cfp.gclose()