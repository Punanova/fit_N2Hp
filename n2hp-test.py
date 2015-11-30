import pyspeckit
from pyspeckit.spectrum.models import n2hp
import numpy as np

import astropy.units as u

rms=3.35E-2
cube = pyspeckit.Spectrum('Core2_cent_N2Hp10.fits', error=np.ones(921)*rms)
cube.xarr.refX = 93173.772e6*u.Hz
cube.xarr.velocity_convention = 'radio'
cube.xarr.convert_to_unit('km/s')
F=False
T=True
import matplotlib.pyplot as plt
plt.ion()
cube.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter,4)
cube.specfit(fittype='n2hp_vtau', guesses=[3.94, 1.0, 0, 0.309], 
    verbose_level=4, signal_cut=3, limitedmax=[F,T,T,T], limitedmin=[T,T,T,T], 
    minpars=[0, 0, -1, 0.05], maxpars=[30.,50.,1,1.0], fixed=[F,F,F,F])
cube.plotter(errstyle='fill')
cube.specfit.plot_fit()
