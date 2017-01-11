#Rajan Patel CMSC 441 hw2.py
########################################################
#Problem 4.1.3
########################################################

import random
import time
#import sys
#print sys.version
#2.7.9 |Anaconda 2.2.0 (64-bit)| (default, Dec 18 2014, 16:57:52) [MSC v.1500 64 bit (AMD64)]
CrossoverPoint = 50
numList = []

#Creates an array of random ints
for x in xrange(0,49):
	numList.append(random.randint(-10,30))

#print numList

def MSABruteForce(array, low, high):
	result = [0,0,-9223372036854775806]
	# left = 0
	# right = 0
	# total = -9223372036854775806

	i = low
	while(i < high):
		currentSum = 0
		j = i
		while(j <high):
			currentSum = currentSum + array[j]
			if(result[2] < currentSum):
				result[0] = i
				result[1] = j + 1
				result[2] = currentSum
			j = j + 1
		i = i + 1

	return result

def MSADivideAndConquer2(array, low, mid, high):

	result = [-1,-1,0]
	currentSum = 0;
	leftSum = -9223372036854775806
	rightSum = -9223372036854775806

	i = mid - 1
	while(i >= int(low)):
		currentSum = currentSum + array[i]
		if(currentSum > leftSum):
			leftSum = currentSum
			result[0] = i
		i = i - 1

	currentSum = 0

	j = mid
	while(j < high):
		currentSum = currentSum + array[j]
		if(currentSum > rightSum):
			rightSum = currentSum
			result[1] = j + 1
		j = j + 1

	result[2] = leftSum + rightSum

	return result

def MSADivideAndConquer(array, low, high):

	if(high == (low + 1)):
		result = [low, high, array[low]]
		return result
	else:
		mid = (low + high)/2
		left = MSADivideAndConquer(array, low, mid)
		right = MSADivideAndConquer(array, mid, high)
		cross = MSADivideAndConquer2(array, low, mid, high)

		if(left[2] >= right[2] and left[2] >= cross[2]):
			return left
		elif(right[2] >= left[2] and right[2] >= cross[2]):
			return right
		else:
			return cross

def MSAMixed(array, low, high):

	if((high - low) < CrossoverPoint):
		return MSABruteForce(array, low, high)
	else:
		#MSADivideAndConquer(array, low, high)
		mid = (low + high) / 2
		left = MSAMixed(array, low, mid)
		right = MSAMixed(array, mid, high)
		cross = MSADivideAndConquer2(array, low, mid, high)

		if(left[2] >= right[2] and left[2] >= cross[2]):
			return left
		if(right[2] >= left[2] and right[2] >= cross[2]):
			return right
		else:
			return cross


#print MSAMixed(numList, 0, len(numList))
#print numList

# start1 = time.clock()
# MSADivideAndConquer(numList, 0, len(numList))
# stop1 = time.clock()
# print "Time D&C"
# print"-------------------"
# print stop1 - start1
# print ""

# start1 = time.clock()
# MSABruteForce(numList, 0, len(numList))
# stop1 = time.clock()
# print "Time brute"
# print"-------------------"
# print stop1 - start1
# print ""


# start1 = time.clock()
# MSAMixed(numList, 0, len(numList))
# stop1 = time.clock()
# print "Time Mixed"
# print"-------------------"
# print stop1 - start1
# print ""


#Calculated avg run time of functions
timeTotal = [0,0,0]
trials = 10000

for x in xrange(1,trials):
	start1 = time.clock()
	MSADivideAndConquer(numList, 0, len(numList))
	stop1 = time.clock()
	timeTotal[0] = timeTotal[0] + (stop1 - start1)

	start1 = time.clock()
	MSABruteForce(numList, 0, len(numList))
	stop1 = time.clock()
	timeTotal[1] = timeTotal[1] + (stop1 - start1)

	start1 = time.clock()
	MSAMixed(numList, 0, len(numList))
	stop1 = time.clock()
	timeTotal[2] = timeTotal[2] + (stop1 - start1)

print "D&C"
print timeTotal[0]/trials

print "brute"
print timeTotal[1]/trials

print "mixed"
print timeTotal[2]/trials

#Results
#------------------------------------------------------------------------------------
# Divide and Conquer:	8.01271791578e-05
# Brute Force:			7.9373660893e-05
# Mixed:				5.08683444124e-05

#With an array size of 49 brute force out preforms divide and conquer on my desktop.
#Mixed outpreforms both divide and conquer and brute force.
#Number of trials = 100,000
#TOTAL RUNTIME: 24.3 seconds

# Divide and Conquer:	0.0263507968127
# Brute Force:			3.00491914591
# Mixed:				0.0239384362226

#With an array size of 10,000 divide and conquer out preforms brute force on my desktop.
#Mixed outpreforms both divide and conquer and brute force.
#Number of trials = 100
#TOTAL RUNTIME: 305.6 seconds
#------------------------------------------------------------------------------------


########################################################
#Problem 4.1.5
########################################################
def fast():	
	#Creates an array of random ints
	for x in xrange(0,10):
		array.append(random.randint(-10,10))

	BestSum = -9223372036854775807
	BestStart = 0
	BestEnd = 0
	localStart = 0
	localSum = 0

	for i in xrange(0,len(array) -1):
		localSum = localSum + array[i]

		if localSum > BestSum:
			BestSum = localSum
			BestStart = localStart
			BestEnd = i

		if localSum <= 0:
			localSum = 0
			localStart = i + 1

	print BestStart
	print BestEnd
	print BestSum
	print array


#Results
#------------------------------------------------------------------------------------
#The fast function run in linear time
#------------------------------------------------------------------------------------