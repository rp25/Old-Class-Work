# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:29:45 2016

@author: RajanPatel
"""

def lam(x1,y1,x2,y2,prime,a):
    if(x1 != x2 and y1 != y2):
        lam = (y2 - y1)*modinv((x2-x1)% prime,prime) % prime
    else:
        lam = (3*x1*x1 + a)*modinv(2*y1 % prime,prime) % prime
        print ("check")
        
    x3 = (lam*lam - x1 - x2) % prime
    y3 = (lam*(x1-x3) - y1) % prime
        
    print ( "x3: " + str(x3) )
    print  ("y3: " + str(y3)   )      
                
        
        
#http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python        
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        
        
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        
        
        
def main():
    print (lam(23,21,4,7,23,1))