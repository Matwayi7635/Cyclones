import matplotlib
matplotlib.use('pdf')#failure to include this results to an error
import cf
import cfplot as cfp
f=cf.read('cfplot_data/ggap.nc')[1]

cfp.gopen(rows=3, columns=3, bottom=0.2)
cfp.gpos(1)
cfp.con(f.subspace(pressure=500), colorbar=None, lines=False, title="top")
cfp.gpos(2)
cfp.mapset(proj='moll')
cfp.con(f.subspace(pressure=500), colorbar=None, lines=False)
cfp.gpos(3)
cfp.mapset(proj='spstere', boundinglat=30, lon_0=180)
cfp.con(f.subspace(pressure=500), colorbar=None, lines=False)
cfp.gpos(4)
cfp.mapset(proj='npstere', boundinglat=30, lon_0=180)
cfp.con(f.subspace(pressure=500), colorbar=None, lines=False, title='500mb')
cfp.gpos(5)
cfp.mapset(proj='spstere', boundinglat=-30, lon_0=0)
cfp.con(f.subspace(pressure=500),lines=False, colorbar_position=[0.1, 0.1, 0.5, 0.02],#olorbar_position=[0.1, 0.1, 0.8, 0.02]
        colorbar_orientation='horizontal')
cfp.setvars(file='multiple.pdf')
cfp.gclose()