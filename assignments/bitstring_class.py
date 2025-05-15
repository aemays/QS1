#!/usr/bin/env python
# coding: utf-8

# # BitString Class 
# 
# Write a Class that implements a bit representation that provides the functionality requested in the following questions.

# In[98]:


# Ensure numpy is imported correctly
import numpy as np
import math
import copy as cp

class BitString:
    """
    Simple class to implement a config of bits
    """
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
            
        











        
        
    


# In[ ]:





# ---
# 
# **1. Create an zero `BitString` of length 8 and flip a few bits and print the output.**
# 
# Methods needed:
# - `__str__()`
# - `flip()`
# - `__len__()`

# In[99]:


my_bs = BitString(8)

my_bs.flip_site(2)
my_bs.flip_site(2)
print(" The following should be 0:")
print(my_bs)

my_bs.flip_site(2)
my_bs.flip_site(7)
my_bs.flip_site(0)

print(" The following should have 0,2,7 bits flipped:")
print(my_bs)

print(" Length of bitstring: ", len(my_bs))
assert(len(my_bs) == 8)


# ---
# 
# **2. Add a method that lets you directly set the value of the bitstring by providing a string of 0s and 1s:**
# 
# Methods needed:
# - `set_config()`

# In[100]:


my_bs = BitString(13)
print(my_bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0]))
print(my_bs)


# ---
# 
# **3. Add a method that returns number of `on` bits and one that returns the number of `off` bits.**
# 
# Methods needed:
# - `on()`
# - `off()`

# In[101]:


print(" on:  ", my_bs.on())
print(" off: ", my_bs.off())
'''
assert(my_bs.on() == 5)
assert(my_bs.off() == 8)
'''


# ---
# 
# **4. Add a method that returns the associated integer (decimal).**
# 
# Methods needed:
# - `integer()`

# In[102]:


print(my_bs.integer())
assert(my_bs.integer() == 3220)


# ---
# **5. Add a method that lets you directly set the value of the bitstring by providing a decimal integer.** 
# 
# Also include  an optional keyword `digits` to let the user specify the length of the string.
# 
# Methods needed:
# - `set_integer_config()`

# In[103]:


my_bs = BitString(20)
my_bs.set_integer_config(3221)

# Let's make sure this worked:
tmp = np.array([0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1])
assert((my_bs.config == tmp).all())

# We can provide an even stronger test here:
for i in range(10):
    my_bs.set_integer_config(i) # Converts from integer to binary
    print(my_bs.set_integer_config(i), "binary form of", i)
    assert(my_bs.integer() == i) # Converts back from binary to integer and tests
    print(my_bs.integer())


# ---
# 
# **6. Overload equality operator**
# 
# Methods needed:
# - `__eq__()`

# In[104]:


my_bs1 = BitString(13)
my_bs1.set_config([0,1,1,0,0,1,0,1,1,0,1,0,0])
print(my_bs1, ": ", my_bs1.integer())

my_bs2 = BitString(13)
my_bs2.set_integer_config(3252)
print(my_bs2, ": ", my_bs2.integer())


assert(my_bs1 == my_bs2)

my_bs2.flip_site(5)
assert(my_bs1 != my_bs2)


# In[ ]:





# In[ ]:




