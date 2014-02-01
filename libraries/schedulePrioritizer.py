'''

http://jsfiddle.net/nvYZ8/1/

'''

from functionChecker import functionChecker

functionChecker("schedulePrioritizer.py", "getAllPossibleSchedules")

"function name: getNonOverlappingRanges"
"requires functions: containsOverlappingRanges, overlapsWithOthers(theArr,theIndex)"
"is defined: True"
"description: Return all ranges in the array that do not overlap with any of the other ranges."

"function name: removeNonOverlappingRanges"
"requires functions: getNonOverlappingRanges"
"is defined: False"
"description: Remove all ranges from the array that do not overlap with any of the other ranges."

"function name: containsOverlappingRanges"
"requires functions: rangesOverlap"
"is defined: True"
"description: Return true if the array contains more than zero overlapping ranges, and otherwise return false."

"function name: rangesOverlap"
"requires functions: False"
"is defined: True"
"description: Check whether two 2D arrays are overlapping ranges."

"function name: convertToBinary"
"requires functions: False"
"is defined: True"
"description: Convert from decimal to binary."

"function name: overlapsWithOthers(theArr,theIndex)"
"requires functions: rangesOverlap"
"is defined: True"
"description: Check whether one element in the array overlaps with at least one of the elements that follows it."

def convertToBinary(x):
    return int(bin(x)[2:])
def rangesOverlap(r1, r2):
	#The events are also considered to be overlapping if one event happens immediately after the other.
	return (r1[0] <= r2[1]) and (r2[0] <= r1[1])

def containsOverlappingRanges(arrayOfRanges):
	for current in arrayOfRanges:
		for current2 in arrayOfRanges:
			if(rangesOverlap(current, current2) and current != current2):
				return True
	return False

def overlapsWithOthers(arr1, index):
	for current in arr1:
		if((current != arr1[index])):
			if(rangesOverlap(current, arr1[index])):
				return True
	return False

def getNonOverlappingRanges(arr1):
	arrayToReturn = []
	for idx, current in enumerate(arr1):
		if(not overlapsWithOthers(arr1, idx)):
			arrayToReturn += [current]
	return arrayToReturn

print convertToBinary(2)
print rangesOverlap([1, 3], [2, 5])
print rangesOverlap([1, 3], [3.1, 5])
print(overlapsWithOthers([[1,3], [4,5], [2,4], [7,8]],3))

print containsOverlappingRanges([[1, 3], [3.1, 5]])
print containsOverlappingRanges([[1, 3], [3.1, 5], [6,8], [1,7]])

print getNonOverlappingRanges([[1, 3], [3.1, 5], [9, 10], [7, 10]])

"function name: getAllPossibleSchedules"
"requires functions: containsOverlappingRanges, convertToBinary"
"is defined: False"
"description: Return true if the array contains more than zero overlapping ranges, and otherwise return false."
def getPossibleSchedules(theArray):
	for current in theArray:
		pass
