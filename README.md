# QS1
This repo is a collection of python notebooks designed to simulate configurations of qubits, calculate their energy among other physicals, and model those systems in different situations

## Bitstring Class
The file bitstring_class.ipynb, is the foundation for the rest of the notebooks. This file's main use is to be able to create arrays (configurations) of bits to the user's liking.
- You can create a string of 0's and 1's to your liking of whatever length you want, by inputting the binary yourself, or using one of the functions in this notebook to convert an integer to a binary string.
  - The user can use the function, integer(configuration), to convert a binary string to its integer counterpart, or they could use the function set_integer_config(integer) to take an integer, convert that integer to binary, and create an array object (the bitstring object) to then experiment with in other files
