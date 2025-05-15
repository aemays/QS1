"""
Class thta

energy(config::BitString)
set_mu(mus::np.array)
compute_average_values(T::int)

"""

from bitstring_class import BitString
import numpy as np
import math
import copy as cp

class IsingHamiltonian:

    
    def __init__(self,G):
        self.G = G
        self.mu = np.zeros(N, dtype=int)
    
    def set_mu(self,mu:np.array):
        self.mu = mu
    def energy(bs: BitString):
        """
        Compute energy of configuration, `bs`
    
            .. math::
                E = \\left<\\hat{H}\\right>
    
        Parameters
        ----------
        bs   : Bitstring
            input configuration
        G    : Graph
            input graph defining the Hamiltonian
        Returns
        -------
        energy  : float
            Energy of the input configuration
        """
        x = 0
        y = 0
        hHat = 0
        term1
        term2 = 0
        J = 0
        for u,v in G.edges():
            J = G.edges[u,v]
            J = J.get('weight')
            if int(bs.config[u]) == 1:
                x = 1
            else:
                x = -1
            if int(bs.config[v]) == 1:
                y = 1
            else:
                y = -1
            term1 += J*x*y
            term2 += self.mu[u] * x
            hHat += term1 + term2
        return hHat


        
            
        













