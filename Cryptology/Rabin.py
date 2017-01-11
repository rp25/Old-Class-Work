# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 02:11:56 2016

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
        
        
#Generates primes given magnitude of the prime        
def generateLargePrimes():
    
#    a = pow(10,size)
#    b = pow(11,size)
    #psuedo random way to prevent the algoritm from returning the same prime    
    i =136014705100004654646465165164165161654656516516544314768716861564168714686168716518618746148616818681769718768186761687168716874198168176816718617687168761876916187169716971968716717684176817468168784146941496841949468406486406406468046480646084684065684064065161988941651119712715970197951071597017951791091

    #print (i)
    primes = []
    counter = 0
    while(1):          
        if(isPrime(i, 7)):
            
            counter = counter + 1
            primes.append(i)
                
        if(counter == 4):
            print (i)
            return primes
        i = i +1
        
        
        
#modexp        
#def f(x,e,m):
#    X = x
#    E = e
#    Y = 1
#    while E > 0:
#        if E % 2 == 0:
#            X = (X * X) % m
#            E = E/2
#        else:
#            Y = (X * Y) % m
#            E = E - 1
#    return Y
        
#Input: InputPlainText
#Output: Mature InputPlainText, This function removes all punction and symbols 
#that are not part of the basic alphabet with the exception of numberical values.
def mIPT(IPT):
    
    mStr = ""
    #Checks to see if character is an letter or number
    for i in range(0, len(IPT)):
        if((ord(IPT[i]) >= 48 and ord(IPT[i]) <= 57) or
            (ord(IPT[i]) >= 65 and ord(IPT[i]) <= 90) or
            (ord(IPT[i]) >= 97 and ord(IPT[i]) <= 122) or
            (ord(IPT[i]) == 32)):                
            #Adds letters and converts them to uppercase
            mStr = mStr + IPT[i].upper()
            
    list(mStr)
    final = ""
    for i in range(0,len(mStr)):
        final = final + str(ord(mStr[i]))
    
    #final = 23
    return int((final))

        
        #196 32773653
#the main encryption function
def rabinEncrypt(plaintext):
    #print (plaintext)
    #prime = generateLargePrimes(2)
    #plaintext = int(str(prime[0]) + str(mIPT(plaintext)) )

    plaintext = int(mIPT(plaintext))

    primes = generateLargePrimes(4)
   # primes[0] = 7
    #primes[1] = 11
    n = primes[0] * primes[1]    
    #print (plaintext)
    ciphertext = (plaintext**2) %n
    #ciphertext = 23
    return primes,ciphertext
    
#7239849324
#the main decryption function
def rabinDecrypt(primes, ciphertext):
    print (ciphertext)
    n = primes[0]*primes[1]

    plaintext =[]
    #MODULAR INVERSE
    P = primes[0]
    Q = primes[1]
    
    PQ = modinv(primes[0],primes[1])
    QP = modinv(primes[1],primes[0])
    
    x = (ciphertext**int((P+1)/4) % P)*Q*(QP) 
    y = (ciphertext**int((Q+1)/4) % Q)*P*(PQ ) 
   
    plaintext.append((-x + y) %n)
    plaintext.append(( x + y) %n)
    plaintext.append((-x - y) %n)
    plaintext.append(( x - y) %n)

    TEXT = int2text(plaintext)
    return TEXT    

    



#http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
    
def int2text(num):
    
    mat = num
    for x in range(0,4):
        
        num = str(mat[x])
        if((len(num) %2) == 0):
            string = ""
            for i in range(0,len(num),2):
                char = int(num[i]+num[i+1])
                #print (char)
                if((char >= 48 and char <= 57) or
                    (char >= 65 and char <= 90) or
                    (char >= 97 and char <= 122) or
                    (char == 32)):
                    string = string + chr(char)
                
            if(int(len(string)) == (len(num)/2)):      
                return string
            
    
    