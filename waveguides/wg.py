# -*- coding: utf-8 -*-

"""
Waveguide classes for use in an external module.

Supported waveguide:
1) Coaxial waveguide        (COAX)
2) Two-wire waveguide       (TWWG)
3) Parallel plate waveguide (PPWG)

Note on terminology: These could be classified as transmission lines
because they consist of two conductors, but since we may be concerned with
higher order modes we call them waveguides.

"""

import math
import scipy.constants as spc
import numpy as np
from materials import cond
from materials import dielec_const

class COAX:
    ''' Constuct a coaxial waveguide object '''
    def __init__(self, a, b, metal, dielec):
        '''\n
        a: inner conductor radius, [unit: m]\n
        b: outer conductor radius, [unit: m]\n
        metal: conductor material, [unit: material]\n
        dielec: dielectric material between conductors, [unit: material]'''
        
        self.a = a
        self.b = b
        self.sigma = cond(metal)
        self.eps = dielec_const(dielec)
        self.mu  = 1*spc.mu_0 # mu_r = 1
        self.L   = self.mu*math.log(b/a)/(2*math.pi)
        self.C   = 2*math.pi*self.eps.real/math.log(b/a)
        
    def get_z0(self, freq):
        ''' Return the characteristic impedance at the specified frequency '''     
        w = 2*np.pi*freq   
        Rs = np.sqrt(w*self.mu/(2*self.sigma))
        R = Rs*(1/self.a + 1/self.b)/(2*math.pi)
        G = 2*math.pi*w*self.eps.imag/math.log(self.b/self.a)     
        
        z0 = np.sqrt((R+1j*w*self.L)/(G+1j*w*self.C))
        return z0
    
    def get_gamma(self, freq):
        ''' Return the complex propagation constant at the specified frequency '''  
        w = 2*np.pi*freq   
        Rs = np.sqrt(w*self.mu/(2*self.sigma))
        R = Rs*(1/self.a + 1/self.b)/(2*math.pi)
        G = 2*math.pi*w*self.eps.imag/math.log(self.b/self.a)
        
        gamma = np.sqrt((R+1j*w*self.L)*(G+1j*w*self.C))
        return gamma  
        
    def get_alpha(self, freq):
        ''' Return the  attenuation coefficient at the specified frequency '''              
        return self.get_gamma(freq).real

    def get_beta(self, freq):
        ''' Return the phase constant at the specified frequency '''         
        return self.get_gamma(freq).imag
        

class TWWG:
    ''' Constuct a two-wire waveguide object '''
    def __init__(self, S, a, metal, dielec):
        '''\n
        S: center-to-center conductor separation, [unit: m]\n
        a: conductor radius, [unit: m]\n
        metal: conductor material, [unit: material]\n
        dielec: dielectric material between conductors, [unit: material]'''        
        
        self.S = S
        self.a = a
        self.sigma = cond(metal)
        self.eps = dielec_const(dielec)
        self.mu  = 1*spc.mu_0 # mu_r = 1
        self.L   = self.mu*math.acosh(S/(2*a))/math.pi
        self.C = math.pi*self.eps.real/math.acosh(S/(2*a))
          
        
    def get_z0(self, freq):
        ''' Return the characteristic impedance at the specified frequency '''     
        w = 2*np.pi*freq
        Rs = np.sqrt(w*self.mu/(2*self.sigma))
        R = Rs/(np.pi*self.a)
        G = (np.pi*w*self.eps.imag)/np.math.acosh(self.S/(2*self.a))
        z0 = np.sqrt((R+1j*w*self.L)/(G+1j*w*self.C))
        return z0
    
    def get_gamma(self, freq):
        ''' Return the complex propagation constant at the specified frequency '''     
        w = 2*np.pi*freq
        Rs = np.sqrt(w*self.mu/(2*self.sigma))
        R = Rs/(np.pi*self.a)
        G = (np.pi*w*self.eps.imag)/np.math.acosh(self.S/(2*self.a))
        
        gamma = np.sqrt((R+1j*w*self.L)*(G+1j*w*self.C))
        return gamma  
        
    def get_alpha(self, freq):
        ''' Return the  attenuation coefficient at the specified frequency '''              
        return self.get_gamma(freq).real

    def get_beta(self, freq):
        ''' Return the phase constant at the specified frequency '''         
        return self.get_gamma(freq).imag
        


class PPWG:
    ''' Constuct a parallel plate waveguide object '''
    def __init__(self, S, T, metal, dielec):
        '''\n
        S: plate separation, [unit: m]\n
        T: plate thickness (or height), [unit: m]\n
        metal: conductor material, [unit: material]\n
        dielec: dielectric material between conductors, [unit: material]'''
        
        self.S = S
        self.T = T
        self.sigma = cond(metal)
        self.eps = dielec_const(dielec)
        self.mu  = 1*spc.mu_0 # mu_r = 1
        self.L   = self.mu*S/T
        self.C   = self.eps.real*T/S
        
    def get_z0(self, freq):
        ''' Return the characteristic impedance at the specified frequency '''     
        w = 2*np.pi*freq   
        Rs = np.sqrt(w*self.mu/(2*self.sigma))
        R = 2*Rs/self.T
        G = w*self.eps.imag*self.T/self.S
        
        z0 = np.sqrt((R+1j*w*self.L)/(G+1j*w*self.C))
        return z0
    
    def get_gamma(self, freq):
        ''' Return the complex propagation constant at the specified frequency '''  
        w = 2*np.pi*freq   
        Rs = np.sqrt(w*self.mu/(2*self.sigma))
        R = 2*Rs/self.T
        G = w*self.eps.imag*self.T/self.S
        
        gamma = np.sqrt((R+1j*w*self.L)*(G+1j*w*self.C))
        return gamma  
        
    def get_alpha(self, freq):
        ''' Return the  attenuation coefficient at the specified frequency '''              
        return self.get_gamma(freq).real

    def get_beta(self, freq):
        ''' Return the phase constant at the specified frequency '''         
        return self.get_gamma(freq).imag