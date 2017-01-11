# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:54:23 2016

@author: RajanPatel
"""

import math
import random
import sys

#Uses the Miller-Rabin algorithm to generate primes
#Takes input n, the number being tested, and a confidence variable k
def isPrime(n, k):
    if(n < 7):    
        #Hard coding the first seven cases
        return[0, 0, 1, 1, 0, 1,1][n]
    s = 0
    d = n -1
    while(d & 1 == 0):
        s = s + 1
        d = d >> 1
        #Uses random number generator for large numbers
        for i in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
            x = pow(i, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        # returns false because n is composite
                        return 0
                    elif x == n - 1:
                        i = 0  
                        break 
                if(i):
                    return 0                       
        return 1
        
#modular exponentiation       
def modexp(a, n, m):
	bits = []
	while n:
		bits.append(n%2)
		n /= 2
	solution = 1
	bits.reverse()
	for x in bits:
		solution = (solution*solution)%m
		if x:
			solution = (solution*a)%m
	return solution
        
        
#Generates primes given magnitude of the prime        
def generateLargePrimes(size):
    
    a = pow(10,size)
    b = pow(11,size)
    #psuedo random way to prevent the algoritm from returning the same prime    
    i = random.randint(a,b)    
    primes = []
    counter = 0
    while(1):          
        if(isPrime(i, 10)):
           
           counter = counter + 1
           primes.append(i)
        if(counter == 2):
            return primes
        i = i +1
        
        
        
#Input: InputPlainText
#Output: Mature InputPlainText, This function removes all punction and symbols 
#that are not part of the basic alphabet with the exception of numberical values.
def mIPT(IPT):
    
    mStr = ""
    #Checks to see if character is an letter or number
    for i in range(0, len(IPT)):
        if((ord(IPT[i]) >= 48 and ord(IPT[i]) <= 57) or
            (ord(IPT[i]) >= 65 and ord(IPT[i]) <= 90) or
            (ord(IPT[i]) >= 97 and ord(IPT[i]) <= 122)
            or (ord(IPT[i]) == 32)):                
            #Adds letters and converts them to uppercase
            mStr = mStr + IPT[i].upper()
        
    return mStr
        
def extendedGCD(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0
    
 #finds d using extended gcd   
def findD(e,primes):
    #primes = generateLargePrimes(100)
    #n = primes[0]*primes[1]
    tn = (primes[0] -1) *(primes[1] -1)
    gcd = extendedGCD(tn,e)
    #print ("gcd")
    #print (gcd)
    return gcd[1]

#converts dec to text
def textConverter(text):
    
    text = str(text)    
    msg = ""
    for i in range(0, len(text),2):
        msg = msg + chr(int(text[i]+ text[i +1]))

    print (msg)

#Does the encryption and decrpytion    
def main():
    msg = "I deserve an A"
    msg = mIPT(msg)
    final = ""
    for i in range(0,len(msg)):
        final = final + str(ord(msg[i]))
    
    final = int(final)
    #7332686983698286693265783265
    print (final)
    primes = generateLargePrimes(100)
    
    n = primes[0]*primes[1]
    e = pow(2,16) +1
    
    d = findD(e,primes)

    print (e*d %n)
    ciphertext = modexp(final, e, n)
     
    print (pow(ciphertext,d,n))
    
    
