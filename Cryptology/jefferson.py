# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 00:04:05 2016

@author: RajanPatel
"""
import numpy as np
import random as rn

alphabetStr = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Key = [6,22,17,15,1,2,16,19,13,3,11,14,10,8,9,7,12,4,18,0,21,5,20,23]
key = [6,22,17,15,1,2,16,19,13,3,11,14,10,8,9,7,12,4,18,0,21,5,20,23]
text = "Send in the flying fish"


    
    
    
def createDiskCipher():
    
    disks =  []
    for i in range(0,24):
        rn.shuffle(alphabetStr)
        disks.append([''.join(alphabetStr),i])
        
    #rn.shuffle(disks)
    return disks
    
    
def encrypt(plaintext, key):
    
    randint = rn.randint(1, 25) 
    plaintext = mIPT(plaintext)
    tool = []   
    wheels = createDiskCipher()
    saveDisks(wheels)
    LetterPos = []
    string = ""
    
    #Arranges wheels in an order
    for i in range(0, len(key)):
        tool.append(wheels[key[i]])
        
    print tool
    plaintext = list(plaintext)    
    for i in range(0, len(plaintext)):
        
        for x in range(0,26):
            if(str(plaintext[i]) == str(tool[i][0][x])):
                LetterPos.append((x + randint)%26)
        
    for i in range(0, len(LetterPos)):

        string = string + tool[i][0][LetterPos[i]]
        
     
    
    return string
    
    
def mIPT(IPT):
    if(len(IPT) > 25):
        print "Error text too long"
    
    mStr = ""
    #Checks to see if character is an letter or number
    for i in range(0, len(IPT)):
        if((ord(IPT[i]) >= 48 and ord(IPT[i]) <= 57) or
            (ord(IPT[i]) >= 65 and ord(IPT[i]) <= 90) or
            (ord(IPT[i]) >= 97 and ord(IPT[i]) <= 122)):                
            #Adds letters and converts them to uppercase
            mStr = mStr + IPT[i].upper()
        
    return mStr
    
    
def inputKey():
    key = input("Enter key with commas: ")
    key = key.split(",")
    
    if(len(key) != 24):
        print "Incorrect key length"
    
    return key
    
    
def saveDisks(disks):
    file = open('workfile', 'w')
    
    for i in range(0, len(disks)):
        file.write(str(disks[i][0]))
    
    file.close()
      
    
def loadDisks():
    
    file = open('workfile', 'r')    
    line = file.read()    
    disks = []
    for i in range(0, len(line)+1,26):
        disks.append(line[i:i+26])         
        
    file.close()
    return disks
    
    
    
def createTool(key):
    disks = loadDisks()
    tool = []
    for i in range(0, len(key)):
       tool.append([disks[key[i]], key[i]]) 
    
    return tool
    
    
def decrypt(text):

    WheelPos = Key #inputKey()
    
    
    tool = createTool(WheelPos)
    
    
    
    
    
#    string = ""
#    print tool
#    for i in range(0, len(letterpos)):
#
#        string = string + tool[i][0][letterpos[i]]
#        
#    return string
#    
    
    