# -*- coding: utf-8 -*-
"""
A small program used for testing the waveguide (wg) module
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from wg import TWWG, COAX, PPWG

# Two-wire waveguide topology
S_twwg = 3.5e-3
a_twwg = 1e-3

# Coax waveguide topology
a_coax = 1e-3
b_coax = 4e-3

# Parallel plate waveguide topology
S_ppwg = 3e-3
T_ppwg = 3e-3

# Material parameters
metallic_material = 'Cu'
dielectric = 'vac'

# Construct waveguide objects with the specified topology
twwg = TWWG(S_twwg,a_twwg,metallic_material,dielectric)
coax = COAX(a_coax,b_coax,metallic_material,dielectric)
ppwg = PPWG(S_ppwg,T_ppwg,metallic_material,dielectric)

# Frequency sweep parameters
f_start = 0.1e12
f_stop  = 3e12
f_N     = 201
f = np.linspace(f_start, f_stop, f_N)

# Obtain the attenuation coefficents
alpha_twwg  = twwg.get_alpha(f)
alpha_coax  = coax.get_alpha(f)
alpha_ppwg  = ppwg.get_alpha(f)

# Change units to dB/cm
alpha_twwg__dB_cm = alpha_twwg * 8.686/100
alpha_coax__dB_cm = alpha_coax * 8.686/100
alpha_ppwg__dB_cm = alpha_ppwg * 8.686/100

# Plotting
matplotlib.rcParams.update({'font.size': 14})
plt.plot(f/1e12,alpha_twwg__dB_cm, linewidth=4, label=r'twwg')
plt.plot(f/1e12,alpha_coax__dB_cm, linewidth=4, label=r'coax')
plt.plot(f/1e12,alpha_ppwg__dB_cm, linewidth=4, label=r'ppwg')
plt.ylabel('attenuation (dB/cm)')
plt.xlabel('frequency (THz)')
plt.legend(loc=2)
plt.grid(True)

#plt.savefig('loss.png', format='png', dpi=800)