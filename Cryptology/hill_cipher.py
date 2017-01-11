# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:53:57 2016

@author: RajanPatel
"""

plaintext =  "CENTRALTOOURFEELINGSOFAWARENESSISTHESENSATIONOFTHEPROGRESSIONOFTIM"
ciphertext = "GKGZRREXCQLCJNPAVIYQTYWSRIREWOAILELPWAFXTMWKBPYRLPGXUAVZKCWKBPYRUG"




import numpy


def mIPT(IPT):
    
    IPT = list(IPT)
    mStr = []
    #Checks to see if character is an letter or number
    for i in range(0, len(IPT)):
        mStr.append((ord(IPT[i]) % 64)-1)
        
    return mStr
    
    
    
def count(m):
    counter = []
    for i in range(0, len(m)):
        if(m[i] in counter):
            pass
        else:
            counter.append(m[i])
            
    return counter
    
    
def brute():
   
    A = []
    B = []
    C = []
    D = []

    for a in range(0,27):
        for b in range(0,27):
            for c in range(0,27):
                for d in range(0,27):
                    q = (a*d) - (b*c)
                    if(q != 0):
                        A.append(a)
                        B.append(b)
                        C.append(c)
                        D.append(d)
                        
                        
                        
    return A,B,C,D
    
    
    
    
    
def round2(A,B,C,D):
    
    p = mIPT(plaintext)
    c = mIPT(ciphertext)
    for i in range(0,len(A)):
        mat = numpy.matrix([[A[i], B[i]], [C[i], D[i]]])
    
        mat2 = numpy.matrix([[p[0]],[p[1]]])
        
        x = numpy.dot(mat,mat2) % 26
        
        
        if(x.item(0) == c[0] and x.item(1) == c[1]):
            #print mat
            
            
            mat2 = numpy.matrix([[p[2]],[p[3]]])
        
            x = numpy.dot(mat,mat2) % 26
            if(x.item(0) == c[2] and x.item(1) == c[3]):
                print mat
    

    
    
    
    
    
    
    
    
    
    