"""
Class thta

energy(config::BitString)
set_mu(mus::np.array)
compute_average_values(T::int)

"""

from . import BitString
import numpy as np
import math
import copy as cp
import networkx as nx
from scipy.special import logsumexp

class IsingHamiltonian:

    def __init__(self, G: nx.Graph):
        self.G = G
        self.mu = np.zeros(G.number_of_nodes(), dtype=int)
    def set_mu(self, mu: np.array):
        self.mu = mu
    def energy(self, bs: BitString):
        self.bs = bs
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
        term1 = 0
        term2 = 0
        J = 0
        for u,v in self.G.edges():
            J = self.G.edges[u,v]
            J = J.get('weight')
            if int(self.bs.config[u]) == 1:
                x = 1
            else:
                x = -1
            if int(self.bs.config[v]) == 1:
                y = 1
            else:
                y = -1
            term1 += J*x*y
            term2 += self.mu[u] * x
            hHat += term1 + term2
        return hHat
    

    def compute_average_values(self, T: int):
        self.T = T
        N = self.G.number_of_nodes()
        self.bs = BitString(N)
        E  = 0.0
        M  = 0.0
        Z  = 0.0
        EE = 0.0
        MM = 0.0
        P = 0.0
        




        # Write your function here!
        #k = 1.380649e-23 #Joules/Kelvin
        k = 1
        B = 1/(k*self.T)
        y = [] #energy list
        x = [] #indice list
        dummy = BitString(N)


        
        for L in range(pow(2,N)):
            x.append(L)
            dummy.set_integer_config(L)
            y.append(self.energy(dummy))

        #eArray = np.array(y)
        #logP = -B * energy(bs,G) - (logsumexp(-B * eArray))
        #P = math.pow(math.e, logP)
        for m in range(2**N):
            self.bs.set_integer_config(m)
            Z += math.e**(-B*self.energy(self.bs))

        for meow in range(2**N):
            self.bs.set_integer_config(meow)
            P = math.e**(-B * self.bs.energy())/Z
            E += self.bs.energy()*P
            EE += self.bs.energy()**2*P


            shawarma = 0
            for numba in self.bs.config:
                if numba == 1:
                    shawarma += 1
                if numba == 0:
                    shawarma += -1
            MM += shawarma**2*P

            M += shawarma * P


        HC = (EE - E**2) * self.T**-2
        
        MS = (MM - M**2) * self.T**-1
        
        return E, M, HC, MS  

        
            
        













