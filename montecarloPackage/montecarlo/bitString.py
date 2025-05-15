# Ensure numpy is imported correctly


import numpy as np
import math
import copy as cp
class BitString:
    
    """Simple class to implement a config of bits"""

    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int)

    def __repr__(self):
        
        out = ""
        for i in self.config:
            out += str(i)
        return out
        

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
    
        return len(self.config)

    def on(self):
        numba = 0
        i = 0
        integerSelf = 0
        for i in self.config:
            integerSelf = int(self.config[i])
            if integerSelf == 1:
                numba += 1
        return numba

    def off(self):
        i = 0
        numbarino = 0
        for i in self.config:
            integerSelf = int(self.config[i])
            if integerSelf == 0:
                numbarino += 1
        return numbarino
        
    def flip_site(self,i):
        self.i = i
        if self.config[i] == 0:
            self.config[i] += 1
        else:
            self.config[i] -= 1
        
    def integer(self):
        
        index = len(self.config) - 1
        n = 0
        i = 0
        dummy = 0
        for i in range(len(self.config)):
            if self.config[i] == 0:
                if dummy == 0:
                    n += 1
            else:
                dummy += 1
                
        self.config = self.config[n:]
        decNum = 0
        m = 0
        index = len(self.config) - 1
        for m in range(len(self.config)):
            if self.config[m] == 1:
                decNum = decNum + math.pow(2, index)
            index -= 1
        return int(decNum)
    #int(decNum)
            
    def set_config(self, s:list[int]):
        self.config = s
        return self.config

    def set_integer_config(self, dec:int):
        
        dec = int(dec)
        
        dummyList = []
        
        while dec >= 1:
            if dec % 2 == 1:
                dummyList.insert(0,1)
            else:
                dummyList.insert(0,0)
            dec = int(dec / 2)
        while len(dummyList) < self.N:
            dummyList.insert(0,0)
        self.config = np.array(dummyList)
        return self.config