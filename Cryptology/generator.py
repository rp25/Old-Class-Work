#!/usr/bin/env python

# Original version by Will Morgan
# Modified to produce unique integers by Chris Marron 
# (as well as some other modifications)

from random import randint
from sys import argv

def generate_unique_ints(num, lower, upper, file):
    """ Generate a file of unique, random integers   """
    """   num   - number of integers to generate     """
    """   lower - lower bound on integers            """
    """   upper - upper bound on integers            """
    """   file  - name of output file                """
    
    dataFile = open(file, "w")
    dataList = {}

    while len( dataList.keys() ) < num:
        dataList[ str( randint( lower, upper) ) ] = True

    intData = sorted( map( int,  dataList.keys() ) )
    for n in intData:
        dataFile.write(str(n) + "\n")


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        