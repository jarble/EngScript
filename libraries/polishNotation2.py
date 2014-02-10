#To do:

#Test everything in polyglotCodeGenerator.py

#Use re.match(expr, stringToSplit).groups() to split a string with its parameters:
#http://stackoverflow.com/questions/18903923/how-to-split-a-string-in-python-without-redundant-output

from __future__ import division

print([i for i in [1,2,3,4,5] if (i % 2 == 0)])

from convertBases import convertBases

import math
import numpy

#from syntaxRules import syntaxRules #This is the file where all the syntax rules are defined

from factors import factors

from copy import copy
from copy import deepcopy


from pyparsing import OneOrMore, nestedExpr

from addParentheses import addParentheses
from addParentheses import addSemicolons

from removeParentheses import removeParentheses
import re
import time

def remove_values_from_list(the_list, val):
	#Remove all occurrences of a value from a list
	return [value for value in the_list if value != val]



def stringToSyntaxTree(theString):
	#This function generates a syntax tree from a string
	return OneOrMore(nestedExpr()).parseString(theString)[0]

def splitWithArrows(theString):
	splitArray = [value for value in re.compile("(<<)|(>>)").split(theString) if value != '' and value != None]
	arrayToReturn = []
	lastCurrent = ""
	for current in splitArray:
		if current == "<<":
			arrayToReturn += ["<<"]
		elif current == ">>" or lastCurrent == "<<":
			arrayToReturn[len(arrayToReturn)-1] += current
		else:
			arrayToReturn += [current]
		lastCurrent = current
	return arrayToReturn

print(splitWithArrows("(<<herp>>).<<derp>>.(<<hello>>)"))

def splitParameterString(theString):
	toReturn = splitWithArrows(theString)
	'''
	for i in range(0, len(toReturn)):
		if(toReturn[i].startswith("$")):
			toReturn[i] = "<<" + toReturn[i][1:len(toReturn[i])] + ">>"
	'''
	#print("The split parameter string: " + str(toReturn))
	return toReturn

def allOccurrences(theList, thingToFind):
	return [i for i, x in enumerate(theList) if x == thingToFind]

def getThingToCheckAgainstRegex(theArray):
	theCounter = 0
	toReturn = ""
	theArrays = []
	for idx, current in enumerate(theArray):
		if(idx != 0):
			toReturn += " "
		if (type(current) != str or (type(current) == str) and (("'" in current) or ('"' in current))):
			theCounter += 1
			toReturn += "<<>>"
			theArrays += [current]
		else:
			toReturn += current
	return {"stringToCheckAgainstRegex":toReturn, "theArrays":theArrays}

def getInfoFromArray(theInputArray, reallyNewInfoArray):
	thingToCheckAgainstRegex = getThingToCheckAgainstRegex(theInputArray)
	
	dictToReturn = {"theArrays":thingToCheckAgainstRegex["theArrays"],"possibleOutputs":[]}
	
	for i in range(0, len(reallyNewInfoArray)):
		infoArrayCopy = copy(reallyNewInfoArray[i])
		regexToCheck = infoArrayCopy["theRegex"]
		infoArrayCopy["splitInputStatement"] = splitStatement(regexToCheck, thingToCheckAgainstRegex["stringToCheckAgainstRegex"])
		if(infoArrayCopy["splitInputStatement"] != None):
			for current in infoArrayCopy["inputToOutput"]:
				for current1 in current[1]:
					infoArrayCopy["splitOutputString"][current1] = infoArrayCopy["splitInputStatement"][current[0]]
			thingToAddToList = [{"output":infoArrayCopy["splitOutputString"], "condition":infoArrayCopy["condition"], "regex":infoArrayCopy["splitInputStatement"]}]
			if not (thingToAddToList in dictToReturn["possibleOutputs"]):
				dictToReturn["possibleOutputs"] += [thingToAddToList]
				dictToReturn["inputToOutput"] = infoArrayCopy["inputToOutput"]
	return dictToReturn
	

def is_number(s):
    if type(s) == list:
		return False
    try:
        float(s)
        return True
    except ValueError:
        return False

def isSeparatedBy(theArray, theString):
	for i in range(0, len(theArray)):
		if(((i + 1) % 2) == 0):
			if(theArray[i] != theString):
				return False
	return True

def tokenizeString(theString):
	if theString.startswith("-"):
		return theString
	else:
		#print("Splitting the string " + theString)
		return filter(None, re.split('(\-\-|\+\+|\]\[|\{\}|\#|\;|\,|\*|\n|\^|\=|\+|\-|\/|%|\}|\{|\.|\]|\[)', theString))
	
def tokenizeList(theList):
	#print("List to tokenize: " + str(theList))
	#tokenizeList(["3+4+ ", [3,3,3]]) should return ["3", "+", "4", "+", [3,3,3]]
	
	#this requires tokenizeString
	
	#use splitStatement(theRegex, stringToSplit) to split the statement
	theNewList = []
	for current in theList:
		if(type(current) != str and len(current) == 0):
			pass
		elif current[0] == "'" or current[0]=='"' or type(current) != str:
			theNewList += [current]
		else:
			current = tokenizeString(current)
			if(type(current) == str):
				theNewList += [current]
			else:	
				theNewList += current
	for i in range(0, len(theNewList)):
		if((i < len(theNewList)) and theNewList[i] == "."):
			if(is_number(theNewList[i - 1]) and is_number(theNewList[i + 1])):
				theNewList[i] = theNewList[i-1] + theNewList[i] + theNewList[i + 1]
				theNewList.pop(i+1)
				theNewList.pop(i-1)
				
	return theNewList

print("\n\n\nTokenizing the list!")
print(tokenizeList(["3.3+3.4", "/", "'3/5+10'", ["3+3"]]))
print("\n\n\n")

def insertIntoList(theList, index, obj):
	theNewList = copy(theList)
	theNewList.insert(index, obj)
	return theNewList

def surroundCurlyBraces(theList):
	#print("The input: " + str(theList))
	if(type(theList) == list):
		if(len(theList) == 1):
			return theList[0]
		if(len(theList) == 4 and theList[1] == "{" and theList[3] == "}"):
			return theList
	startingIndex = None
	endingIndex = None
	for i in range(0, len(theList)):
		if theList[i] == "{":
			startingIndex = i
		elif theList[i] == "}":
			endingIndex = i
			arrayToInsert = [theList[startingIndex-1]] + ["{", "}"]
			#print("Array to insert: " + str(arrayToInsert))
			#print("Array to insert inside array to insert: " + str(theList[startingIndex+1:endingIndex]))
			arrayToInsert.insert(2, theList[startingIndex+1:endingIndex])
			#print("New array to insert: " + str(arrayToInsert))
			theNewList = theList[0:startingIndex-1] + [arrayToInsert] + theList[endingIndex+1:len(theList)]
			#print("The new list: " + str(theNewList))
			return theNewList
	return theList
	#raise Exception("surroundCurlyBraces must be implemented.")
	#To do
	#print(theList)

print surroundCurlyBraces(["hello", [1,2,3,4], "print", "{", "i", "j", "}", ";"])
#print(surroundCurlyBraces(surroundCurlyBraces(["hello", [1,2,3,4], "print", "{", "i", "j", "}", ";"])))

def surroundBrackets(theList):
	#print("The input: " + str(theList))
	if(len(theList) == 3 and theList[0] == "[" and theList[2] == "]"):
		return theList
	#[[3,4],[1,2]] should become [([3,4]),([1,2])]
	lastBracket = ""
	startingIndex = 0
	endingIndex = 0
	theNewArray = []
	arrayToInsert = []
	for i in range(0,len(theList)):
		if theList[i] in ["[", "{"]:
			lastBracket = theList[i]
			startingIndex = i
		if(theList[i] == "]" and lastBracket == "["):
			endingIndex = i
			for j in range(0,len(theList)):
				if(startingIndex+1 <= j <= endingIndex-1):
					arrayToInsert += [theList[j]]
				elif((j != startingIndex) and (j != endingIndex)):
					#else:
					#print("j: " + str(j))
					#print(theList[j])
					theNewArray += [theList[j]]
			#print("Array to insert: " + str(arrayToInsert))
			#return theNewArray
			if(len(arrayToInsert) == 1):
				arrayToInsert = arrayToInsert[0]
			return insertIntoList(theNewArray, startingIndex, ["[", arrayToInsert, "]"])
	return theList
	#print(theList)

def surroundBracesAndBrackets(theList):
	#time.sleep(1)
	if(type(theList) != list):
		theList = list(theList)
	theOldList = copy(theList)
	theList = surroundBrackets(theList)
	theList = surroundCurlyBraces(theList)
	if(theList != theOldList):
		return surroundBracesAndBrackets(theList)
	else:
		return theOldList

#print(surroundCurlyBraces(["[", "3", "{", "hi", "+", "wow", "}", "3", "]"]))


def evaluateMacro(theOldArray, reallyNewInfoArray):
	#print(theOldArray)
	if(type(theOldArray) == str):
		return theOldArray
	theOldArray = tokenizeList(theOldArray)
	
	if(theOldArray[0] == "#"):
		return ""
	
	if(len(theOldArray) == 1 and type(theOldArray[0]) != str):
		return evaluateMacro(theOldArray[0], reallyNewInfoArray)
	if(("[" in theOldArray) or ("{" in theOldArray)):
		theOldArray = surroundBracesAndBrackets(theOldArray)
		
	if(len(theOldArray) > 2) and (";" in theOldArray):
		#print("The old array: " + str(theOldArray))
		theNewArray = [[[]]]
		for i in range(0, len(theOldArray)):
			current = theOldArray[i]
			if(current == ";"):
				theNewArray[len(theNewArray)-1] += [";"]
				if(i < (len(theOldArray) - 1)):
					theNewArray += [[[]]]; 
			else:
				#print(theNewArray[len(theNewArray)-1])
				theNewArray[len(theNewArray)-1][0] += [current]
		return evaluateMacro(theNewArray, reallyNewInfoArray)
	
	if((len(theOldArray) == 2) and (type(theOldArray[1]) != str)):
		#print("The old array is " + str(theOldArray))
		if(theOldArray[1][0] == "["):
			return evaluateMacro(theOldArray[0], reallyNewInfoArray) + evaluateMacro(theOldArray[1], reallyNewInfoArray)
	for current in ["+", "*", "/", "%", "^", ",", ".", ">", "<", ">=", "<=", "==", "]["]:
		if(current == "^"):
			newCurrent = "**"
		else:
			newCurrent = current
		toReturn = ""
		if isSeparatedBy(theOldArray, current) and (not (theOldArray[-1] == current)):
			for i in range(0, len(theOldArray)):
				if(((i + 2) % 2) == 0):
					toReturn += evaluateMacro(theOldArray[i], reallyNewInfoArray)
					if i < (len(theOldArray) -1):
						if(current == ","):
							toReturn += newCurrent+" "
						else:
							toReturn += " "+newCurrent+" "
		if(not (current in [",", "]["])):
			toReturn = "(" + toReturn + ")"
		if (toReturn != "()" and toReturn != ""):
			return toReturn
	#theOldArray = list(theOldArray)
	isAllArrays = True
	for current1 in theOldArray:
		if (type(current1) == str):
			isAllArrays = False
			break;
	if isAllArrays == True:
		toReturn = ""
		for current in theOldArray:
			toReturn += evaluateMacro(current, reallyNewInfoArray) + " "
		return toReturn
		
			
	theArrayString = str(theOldArray)
	theArray = getInfoFromArray(theOldArray, reallyNewInfoArray);
	if(len(theArray["possibleOutputs"]) == 1):
		theArray["output"] = theArray["possibleOutputs"][0][0]["output"]
		theArray["condition"] = theArray["possibleOutputs"][0][0]["condition"]
	else:
	#	joinedOutput = []
	#	for current in theArray["output"]:
	#		joinedOutput += "".join(currentOutput)
	#	for current in range(1, len(joinedOutput)-1):
	#		if(joinedOutput[current] != joinedOutput[current-1]):
		raise Exception("There must be only one possible output. The possible outputs for "+theArrayString+" are: " + str(theArray["possibleOutputs"]))
	#		else:
	#			theArray["output"] = theArray["possibleOutputs"][0][0]["output"]
	#			theArray["condition"] = theArray["possibleOutputs"][0][0]["condition"]
	counter = 0
	oldOutputArray = copy(theArray["output"])
	theArray["output"] = oldOutputArray
	inputToOutput = theArray["inputToOutput"]
	outputArray = copy(theArray["output"]) #the one with the things to be replaced
	theArrays = theArray["theArrays"]
	theSplitString = theArray["possibleOutputs"][0][0]["regex"]
	
	###Start of loop using theSplitString, inputToOutput, theArrays, and outputArray
	counter = 0
	theSplitString = list(theSplitString)
	for j in range(0, len(inputToOutput)):
		inputPosition = inputToOutput[j][0]
		if(theSplitString[inputPosition] == "<<>>"):
			theSplitString[inputPosition] = evaluateMacro(theArrays[counter], reallyNewInfoArray)
			counter += 1
		for k in range(0, len(inputToOutput[j][1])):
			outputPosition = inputToOutput[j][1][k]
			outputArray[outputPosition] = theSplitString[inputPosition]
	return "".join(outputArray)

def getInfoFromString(theRegexString, theOutputString, isFinal, reallyNewInfoArray):
	if(isFinal == "not final"):
		theOutputString = evaluateMacro(stringToSyntaxTree(theOutputString), reallyNewInfoArray)
		isFinal = 'final'
	toReturn = {"inputToOutput":[]}
	theSplitRegexString = splitParameterString(theRegexString)
	theSplitOutputString = splitParameterString(theOutputString)
	theNewSplitRegexString = [value for value in theSplitRegexString if (value != ' ')]
	for x in range(0, len(theSplitRegexString)):
		if theSplitRegexString[x].startswith("<<") and theSplitRegexString[x].endswith(">>"):
			theSplitRegexString[x] = "([^\s]+)"
			#Find a way to exclude something from this regex:
				#^/(?!ignoreme$)(?!ignoreme2$)[a-z0-9]+$
				#^/(?!ignoreme|ignoreme2|ignoremeN)([^\s]+)$
	for x in range(0, len(theNewSplitRegexString)):
		if theNewSplitRegexString[x].startswith("<<") and theNewSplitRegexString[x].endswith(">>"):
			toReturn["inputToOutput"] += [[x, allOccurrences(theSplitOutputString, theNewSplitRegexString[x])]]
	toReturn["splitOutputString"] = theSplitOutputString
	toReturn["theRegex"] = re.compile("\("+"".join(theSplitRegexString)+"\)")
	return toReturn
	
def splitStatement(theRegex, stringToSplit):
	stringToSplit = "(" +stringToSplit+ ")" 
	toReturn = re.match(theRegex, stringToSplit)
	if(toReturn == None):
		return toReturn
	else:
		return toReturn.groups()

def syntaxInLanguage(syntaxRules, theLanguage):
	syntaxRules1 = deepcopy(syntaxRules)
	theUndefinedThings = []
	for i in range(0, len(syntaxRules1)):
		#print(syntaxRules1[i])
		if type(syntaxRules1[i][1]) is dict:
			if theLanguage in syntaxRules1[i][1].keys():
				syntaxRules1[i][1] = syntaxRules1[i][1][theLanguage]
			else:
				theUndefinedThings += [syntaxRules1[i][0][0]]
				syntaxRules1[i][1] = "Not yet defined for "+theLanguage+" in syntaxRules.py: " + syntaxRules1[i][0][0].replace("<<", "").replace(">>", "")
	'''
	if len(theUndefinedThings) > 0:
		print("In syntaxRules.py, these things are undefined in the language " + theLanguage + ":")
		for current in theUndefinedThings:
			print("	" + current)
	'''
	return syntaxRules1

def makeReallyNewInfoArray(theInfoArray, theLanguage):
	reallyNewInfoArray = []
	theInfoArray = syntaxInLanguage(theInfoArray, theLanguage)
	for i in range(0, len(theInfoArray)):
		if(len(theInfoArray[i]) == 2):
			theInfoArray[i][1] = "(" + theInfoArray[i][1] + ")"
			theInfoArray[i] += ["not final"]
		for j in range(0, len(theInfoArray[i][0])):
			newInfoArray = getInfoFromString(theInfoArray[i][0][j], theInfoArray[i][1], theInfoArray[i][2], reallyNewInfoArray);
			newInfoArray["condition"] = "final";
			reallyNewInfoArray += [newInfoArray];
	return reallyNewInfoArray
print("Getting info from input array")

#reallyNewInfoArray = makeReallyNewInfoArray(syntaxRules)

def getStringOutput(toTest, reallyNewInfoArray):
	#print(toTest)
	toTest = "(" + addParentheses(toTest) + ")"
	#print(toTest)
	return evaluateMacro(stringToSyntaxTree(toTest), reallyNewInfoArray)

def testMacro(toTest, reallyNewInfoArray):
	toTest = addSemicolons(toTest) #This doesn't seem to work properly
	#print(toTest)
	#print("\n")
	theOutput = getStringOutput(toTest, reallyNewInfoArray)
	#print(toTest + " becomes " + theOutput)
	#evaluatedOutput = str(eval(theOutput))
	#print("It evaluates to " + str(eval(theOutput)))
	toTest = theOutput.rstrip().split('\n')
	theIndentation = 0
	finalString = ""
	#print("The split string:" + str(toTest))
	for current in range (0, len(toTest)):
		if toTest[current] == "#indent":
			theIndentation += 1
		elif toTest[current] == "#unindent":
			theIndentation -= 1
		else:
			toTest[current] = toTest[current].strip()
			for current1 in range(0, theIndentation):
				toTest[current] = "	" + toTest[current]
			finalString += toTest[current] + "\n"
	#print("The new split string:\n" + finalString)
	return finalString
	#exec finalString
	#print("The macros are defined in syntaxRules.py.")

'''
testMacro("7 divided by (the sum of (4 + 1) and (5 ^ 7))")
testMacro("foo equals bar")
testMacro("foo += bar")
testMacro("goo ++")
testMacro("foo > bar")
testMacro("foo times bar")
testMacro("foo --")
testMacro("if foo then bar")
testMacro("bar if and only if foo")
testMacro("gorf is greater than borp")
testMacro("(foo to the power of bar) is greater than (foo / bar)")
testMacro("foo unless bar")
testMacro("goof ** gosh")
testMacro("16 is a multiple of 8")
testMacro("if x then y")
testMacro("herp while derp")
testMacro("herp until derp")
testMacro("change 100 to base 2 from base 10")
testMacro("7 divided by (the sum of (4 plus 1) and 5)")
testMacro("function goo parms woof")
testMacro("elif foo then bar")
testMacro("gorf minus bog")
testMacro("switch conditions statements")
testMacro("for foo bar baz biff")
testMacro(
for foo from bar to baz
	if (the product of bar and baz) then
		baz

)
testMacro("(3 ++) ++")
testMacro("[ hi ]")
testMacro("case 5 hello")
testMacro("default hello")
testMacro('((3 + 1) - 4) + (5 to the power of 7)')
testMacro('(3 + 2) + 1')
testMacro("goof ^= woof")
testMacro(

if (3 is a factor of 9)
	(9 is divisible by 3)
)
testMacro(

for foo from bar to baz
	(
	unless goof
		woof
	,
	if goof
		woof
	)

)


testMacro("(the sum of 3 and 4) divided by (the product of 3 and 4)")
testMacro("(a random number)")
testMacro("(replace each 'l' inside 'hello' with 'r')")
testMacro("(random number between 1 and 5)")
testMacro("1.4 rounded to the nearest integer")
testMacro("round 1.4 to the nearest integer")
testMacro("a random number between 5 and 7")
testMacro("round 7.5 up")
testMacro("7.5 rounded up")
testMacro("round 7.5 down")
testMacro("7.5 rounded down")
testMacro(

for every foo in bar
	(console.log { (foo rounded up) })
)
testMacro("foo { bar }")
testMacro("the length of foo")
testMacro("substring of 'hello world' from 1 to 5")

testMacro("foo >= bar")
testMacro("foo <= bar")

testMacro(
"(alert { (substring of 'hello world' between 1 and 5) })"
)

testMacro(

for foo between 1 and 5
	alert { foo } ;
)

testMacro("7 is less than or equal to 6")

testMacro(
for i from 1 to 10
	alert { (random number between 1 and 5) } ;
)

testMacro(

	divide foo recursively into 2 by 2 arrays

)

testMacro(

	recursively divide foo into 2 by 2 arrays

)
testMacro("the regex foo matches the string bar")
testMacro("the string bar matches the regex foo")

testMacro("(alert { foo }) while (the string foo matches the regex bar)")
testMacro("each match of the regex foo in the string boo")
testMacro("20 percent of 50")

testMacro("(return lulz) ;")

testMacro(

function lulz (foo , bar , baz)
	list goof = 
		3 ,
		4 ,
		5 ,
		6
	baz = foo ;
	alert { "Hi!" } ;
	if (x == 3)
		print { (x to the power of 3) } ;
	elif (x == 3)
		print { x } ;
def lulz1 (foo , bar , baz)
	while foo
		foo ;
		bar ;
		baz ;
	for all x from 1 to 5
		print { x } ;
		unless (x is divisible by 3)
			print { x } ;

)


testMacro("(x + y + z) (3 + 4 + (5 to the power of 7))")

testMacro("3 ,")

testMacro(

associative array hello
	(3 --> 3) , (4 --> 5) , (herp --> derp)
array hi
	derp , derp , herp
)

testMacro(
	function hello only returns "Hi!"
)

testMacro(

self-invoking function
	return 3
;

)

testMacro(

bar is in foo

)
'''

'''
import pdb
pdb.run("testMacro('(((3 + 1) - 4) + (5 to the power of 7))')")
'''

#print(surroundBracesAndBrackets(['print', '{', 'derp', '{', 'derp', '{', "3", "+", "4", '}', '}', '}', '+', "[", "hi", "+", "bye", "]"]))

#print(surroundBracesAndBrackets(["[", "3", "[", "hi", "+", "hi", "]", "3", "{", "3", "+", "3", "}", "]"]))

print(surroundBracesAndBrackets(["print", "{","10", "percent", "of", "100", "}", ";"]))
