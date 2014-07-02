'''
Created on Jul 2, 2014

@author: viejoemer

I can print a dict as a string in Python?

¿Yo puedo  imprimir un dict como un string en Python?

str(dict) Produces a printable string representation of a dictionary, but 
this not work for JSON format.
'''

#Definition of a dictionary
d = {'three': 3, 'two': 2, 'one': 1}
print(type(d))
print(d)


#Print a dict like a string
s = str(d)
print(type(s))
print(s)