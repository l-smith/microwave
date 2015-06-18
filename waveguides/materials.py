# -*- coding: utf-8 -*-
#
# Small material library containing material constants
# obtained from Microwave Engineering by Pozar.
#
# These parameters are for the microwave region,
# therefore they will not be useful in the optical region.
# Use Johnson & Christry or other source for optical region.
#
# Double check the values here because it's that I 
# may have typed them in wrong.
#
# Author: Levi Smith 2015
#

import scipy.constants as spc

def cond(material):
    ''' Returns the conductivity of the specified material at 20 deg C. \n
    Example: cond('cu'), cond('gold'), cond('Ag')\n\n
    Reference: Microwave Engineering 4th ed, David Pozar 
    '''
    
    if (material.lower() == 'cu') or (material.lower() == 'copper'):
        return 5.813e7
    elif (material.lower() == 'pec') or (material.lower() == 'perfect_electric_conductor'):
        return 1e30    
    elif (material.lower() == 'au') or (material.lower() == 'gold'):
        return 4.098e7
    elif (material.lower() == 'al') or (material.lower() == 'aluminium') or (material.lower() == 'aluminum'):
        return 3.816e7
    elif (material.lower() == 'ag') or (material.lower() == 'silver'):
        return 6.173e7
    elif (material.lower() == 'brass'):
        return 2.564e7
    elif (material.lower() == 'bronze'):
        return 1.00e7
    elif (material.lower() == 'chromium') or (material.lower() == 'cr'):
        return 3.846e7
    elif (material.lower() == 'water') or (material.lower() == 'h2o'):
        return 2e-4
    elif (material.lower() == 'germanium') or (material.lower() == 'ge'):
        return 2.2e6
    elif (material.lower() == 'graphite'):
        return 7e4
    elif (material.lower() == 'iron') or (material.lower() == 'fe'):
        return 1.03e7
    elif (material.lower() == 'mercury') or (material.lower() == 'hg'):
        return 1.04e6
    elif (material.lower() == 'lead') or (material.lower() == 'pb'):
        return 4.56e6
    elif (material.lower() == 'nichrome'):
        return 1.0e6
    elif (material.lower() == 'nickel') or (material.lower() == 'ni'):
        return 1.449e7
    elif (material.lower() == 'platinum') or (material.lower() == 'pt'):
        return 9.52e6
    elif (material.lower() == 'seawater'):
        return 4
    elif (material.lower() == 'silicon') or (material.lower() == 'si'):
        return 4.4e-4
    elif (material.lower() == 'steel_silicon'):
        return 2e6
    elif (material.lower() == 'steel_stainless'):
        return 1.1e6
    elif (material.lower() == 'solder'):
        return 7e6
    elif (material.lower() == 'tungsten') or (material.lower() == 'w'):
        return 1.825e7
    elif (material.lower() == 'zinc') or (material.lower() == 'zn'):
        return 1.67e7
    else:
        print("Error: material '" + material + "' is currently not supported in function 'cond(material)'.")
    
def dielec_const(material):
    ''' Returns the complex dielectric constant of the specified material at 20 deg C. \n 
    *** BE CAUTIOUS OF THE NEGLECTED FREQUENCY DEPENDANCE ***\n
    These values are obtained from various points between 3-10GHz\n
    Example: dielec_const('pe'), dielec_const('teflon'), dielec_const('vac')\n\n
    Reference: Microwave Engineering 4th ed, David Pozar    
    '''
    eps_0 = spc.epsilon_0  
        
    if (material.lower() == 'pe') or (material.lower() == 'polyethylene'):
        return complex(2.25*eps_0,-2.25*eps_0*0.0004)
    elif (material.lower() == 'vacuum') or (material.lower() == 'vac'):
        return complex(1*eps_0,0)
    elif (material.lower() == 'gaas') or (material.lower() == 'galliumarsenide'):
        return complex(13*eps_0,-13*eps_0*0.006)
    elif (material.lower() == 'teflon') or (material.lower() == 'ptfe'):
        return complex(2.08*eps_0,-2.08*eps_0*0.0004)
    elif (material.lower() == 'silicon') or (material.lower() == 'si'):
        return complex(11.9*eps_0,-11.9*eps_0*0.004)
    elif (material.lower() == 'polystyrene') or (material.lower() == 'ps'):
        return complex(2.54*eps_0,-2.54*eps_0*0.00033)
    else:
        print("Error: material '" + material + "' is currently not supported in function 'dielec_const(material)'.")
    

    