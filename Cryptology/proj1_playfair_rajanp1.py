# -*- coding: utf-8 -*-
#Python 2.7.9 |Anaconda 2.2.0 (64-bit)| (default, Dec 18 2014, 16:57:52) [MSC v.1500 64 bit (AMD64)]
"""
Created on Tue Mar 08 21:23:15 2016

@author: RajanPatel
"""
#Number 1: Playfair

import numpy as np
import difflib

alphabetStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
InputPlainText = "!@#$%^&*()-=' 0123456789It may be unfair, but what happens in a few days, sometimes even a single day, can change the course of a whole lifetime"
InputPlainText2 = " Hello Good morning1"

#Input: InputPlainText
#Output: Mature InputPlainText, This function removes all punction and symbols 
#that are not part of the basic alphabet with the exception of numberical values.
def mIPT(IPT):
    
    mStr = ""
    #Checks to see if character is an letter or number
    for i in range(0, len(IPT)):
        if((ord(IPT[i]) >= 48 and ord(IPT[i]) <= 57) or
            (ord(IPT[i]) >= 65 and ord(IPT[i]) <= 90) or
            (ord(IPT[i]) >= 97 and ord(IPT[i]) <= 122)):                
            #Adds letters and converts them to uppercase
            mStr = mStr + IPT[i].upper()
        
    return mStr
        
#Input: key
#Output: playfair matrix
def createMatrix(key):
    #Creates a mature key by removing all non alphanumeric characters
    mKey = checkKey(key)    
    #checks to see if key is longer than 36 characters
    if(len(key) > 36):
        print ("Key too long.")
        
    mAlphabetStr = ""
    #Need to remove repeating characters in keys 
    mAlphabetStr = alphabetStr.translate(None, mKey)
    mKey = mKey + mAlphabetStr
    mKey = list(mKey)
    matrix = np.asarray(mKey)
    #Creates a 6 x 6 matrix with key
    matrix = np.reshape(matrix, (6, 6))
    return matrix
        
#Input: Raw key 
#Output: Mature key, This function removes repeating alphanumeric characters
def checkKey(key):
    
    key = mIPT(key)    
    for i in range(1,len(key)-1):
        if(key[i] in key[:i]):            
            key = key[:i] + " " + key[i+1:]             
    key = mIPT(key)
    return key 
    
    
#Input: plaintext, and key
#Output: cipher 
def encrypt(plaintext, key):
    
    cipher = ""
    matrix = createMatrix(key)
    plaintext = mIPT(plaintext)
    #Makes the plaintext length even
    if(len(plaintext)%2 == 1):
        plaintext = plaintext + 'Z'
    
    for i in range(0,len(plaintext),2):
        
        firstLetterLocation = np.where(matrix==plaintext[i])
        secondLetterLocation = np.where(matrix==plaintext[i+1])   
        #Adds X if two consecutive letters are repeating
        if(plaintext[i] == plaintext[i+1]):
            cipher = cipher + plaintext[i] + 'X'
        #Shift two letter to the right if both letters are in the same row    
        elif(firstLetterLocation[0][0] == secondLetterLocation[0][0]):
            cipher = cipher + matrix[firstLetterLocation[0][0],(firstLetterLocation[1][0]+1) %6]
            cipher = cipher + matrix[secondLetterLocation[0][0],(secondLetterLocation[1][0]+1) %6]
        #Shift two letter down if both letter are in the same column                          
        elif(firstLetterLocation[1][0] == secondLetterLocation[1][0]):
            cipher = cipher + matrix[(firstLetterLocation[0][0]+1) %6,firstLetterLocation[1][0]]
            cipher = cipher + matrix[(secondLetterLocation[0][0]+1) %6,secondLetterLocation[1][0]]
        #Replaces two letters with its opposite corner of the rectangle    
        else:
            firstLocation = [firstLetterLocation[0][0],firstLetterLocation[1][0]]
            secondLocation = [secondLetterLocation[0][0],secondLetterLocation[1][0]]
            cipher = cipher + matrix[firstLocation[0],secondLocation[1]]
            cipher = cipher + matrix[secondLocation[0],firstLocation[1]]
            
    return cipher
    
    
    
    
def decrypt(cipher, key):    
    
    plaintext = ""
    matrix = createMatrix(key)
    cipher = mIPT(cipher)
    
    for i in range(0,len(cipher),2):
        
        firstLetterLocation = np.where(matrix==cipher[i])
        secondLetterLocation = np.where(matrix==cipher[i+1])   
        #Attempts to correct for double letters in the plaintext
        if('X' == cipher[i+1]):
            #print cipher[i]
            plaintext = plaintext + cipher[i] + cipher[i]
        #Reverse row shift
        elif(firstLetterLocation[0][0] == secondLetterLocation[0][0]):
            plaintext = plaintext + matrix[firstLetterLocation[0][0],(firstLetterLocation[1][0]-1) %6]
            plaintext = plaintext + matrix[secondLetterLocation[0][0],(secondLetterLocation[1][0]-1) %6]
        #Reverse column shift
        elif(firstLetterLocation[1][0] == secondLetterLocation[1][0]):
            plaintext = plaintext + matrix[(firstLetterLocation[0][0]-1) %6,firstLetterLocation[1][0]]
            plaintext = plaintext + matrix[(secondLetterLocation[0][0]-1) %6,secondLetterLocation[1][0]]
        #Reverse rectangle shift
        else:
            firstLocation = [firstLetterLocation[0][0],firstLetterLocation[1][0]]
            secondLocation = [secondLetterLocation[0][0],secondLetterLocation[1][0]]
            plaintext = plaintext + matrix[firstLocation[0],secondLocation[1]]
            plaintext = plaintext + matrix[secondLocation[0],firstLocation[1]]
    
    return plaintext
    
    
  
   
    
    
#def writeFile(text):
#    file = open('workfile', 'w')
#    
#    file.write(text)    
#    file.close()   
#    
#    
#def readFile():
#    
#    file = open('workfile', 'r')    
#    line = file.read()  
#    
#    file.close()
#    return line    
    

def main():
    
    key = input("Enter key as string: ")  
    plaintext = input("Enter alphanumeric plaintext as string: ")
    
    cipher = encrypt(plaintext, key)    
    print (cipher)
    print (decrypt(cipher, key))
    
   
# AX pair is assumed to be double As    
   