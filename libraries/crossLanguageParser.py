#This version is obsolete! Use polishnotation.py instead.
#Test everything in polyglotCodeGenerator.py

from listOfRegexes import *
from copy import copy, deepcopy
import random
from random import randint
from random import choice
from pyparsing import OneOrMore, nestedExpr
import numpy
import re;
from addParentheses import addParentheses
from removeParentheses import removeParentheses

def addOpeningAndClosingParentheses(theString):
	if(theString.startswith("(") == False):
		theString = theString + "("
	if(theString.endswith(")") == False):
		theString = theString + ")"
	return theString

"function name: numberOfIndentations(theString)"
"requires functions: False"
"is defined: True"
"description: Get the number of indentations at the beginning of the string."

"function name: addInitialParentheses(theString,numberOfParentheses)"
"requires functions: numberOfIndentations(theString)"
"is defined: True"
"description: Add parentheses to beginning of the string after the indentation."

#print addInitialParentheses("				lol herp de derp", 4)

"function name: addFinalParentheses(theString,numberOfParentheses)"
"requires functions: False"
"is defined: True"
"description: Add parentheses to the end of the string."

"function name: addParentheses(theString)"
"requires functions: numberOfIndentations(theString), addFinalParentheses(theString,numberOfParentheses), addInitialParentheses(theString,numberOfParentheses)"
"is defined: True"
"description: Add parentheses to the string to match the indentation."

#print(addParentheses(
'''
while (i > 0)
	(print 'hello')
	(print 'hello')
	while (i > 5)
	
		print
			'"world"'
'''
#))

"function name: evaluateMacro"
"requires functions: evaluateMacroWithSpecificString(inputString,variableNames,stringToReturn), addParentheses(theString)"
"is defined: False"
"description: Return the output of the macro."

"function name: splitMacroWithParentheses"
"requires functions: replaceParenthesesWithSymbols(theString), getExpressionsInParentheses(theString)"
"is defined: True"
"description: Split the macro with parentheses using a regular expression."

"function name: replaceParenthesesWithSymbols(theString)"
"requires functions: False"
"is defined: True"
"description: Replace the symbols inside nested parentheses with <<>>."

"function name: getExpressionsInParentheses(theString)"
"requires functions: False"
"is defined: True"
"description: Get an array of every substring in the input that is inside parentheses."

"function name: replaceMultipleStringsWithMultipleStrings"
"requires functions: False"
"is defined: True"
"description: Replace multiple strings in a string with multiple other strings."

functionChecker("crossLanguageParser.py", "evaluateMacro")

'''

http://stackoverflow.com/questions/18903923/how-to-split-a-string-in-python-without-redundant-output

Here's a demonstration of parameters being extracted from a macro.
Put ?: in front of every group, like this: (?:foo|bar|baz). Otherwise it will produce redundant results in the output.
'''


#An example of an array that defines a list of regular expressions to match a pattern:
patternDefiningArray = [
	[
		["theArray", '(rotated(?: by|))' "theDegrees", '(degrees)'],
		["(rotation of)", "theArray", "by", "theDegrees", "degrees"]
	],
	["theArray", "theDegrees"],
	["rotateArray(", "theArray", ", " "theDegrees", ")"]
]

def replaceMultipleStringsWithMultipleStrings(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

#print(replaceMultipleStringsWithMultipleStrings("foo and bar are baz", {"foo":"1", "bar":"2", "baz":"3"}))

def lisp(x): #convert parse array back into symbols
	newStr = ""
	for current in x:
		if(type(current) == str):
			newStr += " " + current
		else:
			newStr += " " + lisp(current)
	newStr = newStr[1:len(newStr)]
	return "("+newStr+")"
def getExpressionsInParentheses(theString):
	#print("Get the expressions for: " + theString)
	theData = OneOrMore(nestedExpr()).parseString(theString)
	theNewArr = []
	for current in theData[0]:
		if(type(current) != str):
			theNewArr += [lisp(current)]
	return theNewArr

def replaceParenthesesWithSymbols(theString):
	#theString = addOpeningAndClosingParentheses(theString)
	#print("The thing to replace with symbols is " + theString)
	theData = OneOrMore(nestedExpr()).parseString(theString)
	theNewString = ""
	for current in theData[0]:
		if(type(current) == str):
			theNewString += " " + current
		else:
			theNewString += " <<>>"
	theNewString = "(" + theNewString[1:len(theNewString)] + ")" 
	return theNewString

aStringToPrint = "(replace (foo) in bar with (substring from 2 to 3 in (a string called 'hello')))"
#print(replaceParenthesesWithSymbols(aStringToPrint))
#print(getExpressionsInParentheses(aStringToPrint))

def printMatches(stringToMatch):
	stringToMatch = replaceParenthesesWithSymbols(stringToMatch)
	toReturn = []
	#theArray is an array of regular expressions that is defined in listOfRegexes.py
	for current in theArray:
		if(current.match(stringToMatch)):
			theSplitString = re.match(current, stringToMatch).groups()
			#theArgs = 
			toReturn += [{"splitString":theSplitString, "matchingRegex":current}]
	#if(toReturn == []):
		#raise Exception(stringToMatch + " does not match any regular expression.")
	return toReturn

def my_shuffle(array):
	random.shuffle(array)
	return array

def getMatchingRegex(theString1):
	theString1 = replaceParenthesesWithSymbols(theString1)
	thingToReturn = printMatches(theString1)[0]["matchingRegex"]
	return thingToReturn

def splitMacroWithParentheses(theString):
	theExpressions = getExpressionsInParentheses(theString)
	theString = replaceParenthesesWithSymbols(theString)
	#print(theString)
	#print(theExpressions)
	theSplitString = list(printMatches(theString)[0]["splitString"])
	theCounter = 0
	for idx, current in enumerate(theSplitString):
		if(current == "<<>>"):
			theSplitString[idx] = theExpressions[theCounter]
			theCounter += 1
	return theSplitString

#splitMacroWithParentheses("(replace (substring of 'hello' between 2 and 3) in (bar is an integer) with (baz is not a string))")

#splitMacroWithParentheses("(substring of (gorp is really funny) between (3 is a magic (it's a number)) and (4 is an integer))")

def rangesOverlap(arr1, arr2):
	if (arr1[0] <= arr2[1]) and (arr2[1] <= arr2[1]):
		return True
		
def arrayDimensions(theArr):
	return numpy.array(theArr).shape
	
#print(evaluateMacroWithSpecificString("(replace (substring of 'hello' between 2 and 3) in (bar is an integer) with (baz is not a string))"))

def sumOfAllNums(theNumArr):
	toReturn = 0
	for current in theNumArr:
		toReturn += current
	return current

def splitMacroWithWhitespace(theString):
	theExpressions = getExpressionsInParentheses(theString)
	theString = replaceParenthesesWithSymbols(theString)
	#print(theString)
	#print(theExpressions)
	theSplitString = OneOrMore(nestedExpr()).parseString(theString)[0]
	theCounter = 0
	for idx, current in enumerate(theSplitString):
		#print("The string here is " + current)
		if(current == '<<>>'):
			#print("Replacing " + theSplitString[idx] + " with " + theExpressions[theCounter])
			theSplitString[idx] = theExpressions[theCounter]
			theCounter += 1
	return theSplitString

def getNonSeparatorParts(theString):
	theNewArr = []
	theSplitString = splitMacroWithWhitespace(theString)
	for idx, current in enumerate(theSplitString):
		if(((idx + 1)%2) != 0):
			theNewArr += [current]
	return theNewArr

def everyOtherIsTheSame(theSplitString):
	firstCurrent = theSplitString[1]
	if(len(theSplitString) % 2 == 0):
		return False
	for idx, current in enumerate(theSplitString):
		if((idx+1)%2 == 0):
			if(current != firstCurrent):
				return False
		else:
			if(current == firstCurrent):
				return False
	return True

def isArithmeticOperator(theString):
	if theString in ["+", "-", "-", "/", "^", "%", "&", "and", "or", "<", ">", "<=", ">=", "==", "||"]:
		return True
	return False

"function name: getDictionaryFromMacro(theVariables,theMacro,theResult)"
"requires functions: splitMacroWithParentheses, replaceParenthesesWithSymbols(theString)"
"is defined: True"
"description: Return the output of the macro. Replace the variables in stringToReturn with the parameters"

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def removeEachValueFromList(the_list, values):
	for current in values:
		the_list = remove_values_from_list(the_list, current)
	return the_list

def getDictionaryFromMacro(theVariables, theMacro, theResult):
	arrayOfVariables = theVariables.split(",")
	newArrayOfVariables = deepcopy(arrayOfVariables)
	newArrayOfVariables += ["\(", "\)"]
	theVariables = "(" + "|".join(newArrayOfVariables) + ")"
	#how to get the index of a string in another string: string.index('stringToFind')
	#how to split a string without removing separators: http://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators
	
	theSplitMacro = re.split(theVariables, theMacro)
	
	theSplitMacro = filter(None, theSplitMacro)
	theSplitMacro = removeEachValueFromList(theSplitMacro, ["", ")", "("])
	
	theSplitResult = re.split(theVariables, theResult)
	theSplitResult = removeEachValueFromList(theSplitResult, ["", ")", "("])

	#print(theSplitMacro)
	#print(theSplitResult)
	
	#print(theSplitMacro.index("bar"))
	#print(arrayOfVariables)
	dictionaryToReturn = {}
	
	for current in arrayOfVariables:
		dictionaryToReturn[theSplitMacro.index(current)] = theSplitResult.index(current) 
	return dictionaryToReturn
	

#print(getDictionaryFromMacro('foo,bar', '(foo equals equals bar)', '(foo == bar)'))

def is_prime(a):
    return all(a % i for i in xrange(2, a))

#return am

#print(removeParentheses("(print (the type of foo))", "foo"))
#print(removeParentheses("((foo [bar]) = baz)","foo,bar"))

def getMacroParameters(inputString,stringThatMatchesRegex,variableNames,stringToReturn, returnParameters = False):
	#print("Input string: " + inputString)
	#print("String that matches regex: " + stringThatMatchesRegex)
	#print("variable names: " + variableNames)
	#print("string to return: " + stringToReturn)
	#Return None if the input doesn't match a regex.
	if(printMatches(replaceParenthesesWithSymbols(inputString)) == []):
		return None
	if(printMatches(replaceParenthesesWithSymbols(stringThatMatchesRegex)) == []):
		#raise Exception(stringThatMatchesRegex + " does not match any regular expression.")
		return None
	if(getMatchingRegex(replaceParenthesesWithSymbols(stringThatMatchesRegex))) != getMatchingRegex(replaceParenthesesWithSymbols(inputString)):
		return None
	
	#print(replaceParenthesesWithSymbols(inputString))
	#print(getExpressionsInParentheses(inputString))
	theSplitInputString = splitMacroWithParentheses(inputString)
	theSplitParameterString = splitMacroWithParentheses(stringThatMatchesRegex)
	
	
	arrayOfVariables = variableNames.split(",")
	
	#print("theSplitInputString: " + str(theSplitInputString))
	#print("theSplitParameterString: " + str(theSplitParameterString))
	#print("theSplitStringToReturn: " + str(theSplitStringToReturn))
	#print("arrayOfVariables: " + str(arrayOfVariables))
	
	parameterInformationDictionary = {}
	
	#The location of each variable in theSplitInputString is the same as the location of each variable in the
	for current in arrayOfVariables:
		for idx, current1 in enumerate(theSplitParameterString):
			#print(current + ", " + current1)
			if current1 in current:
				parameterInformationDictionary[current] = theSplitInputString[idx]
	
	#print("parameterInformationDictionary: " + str(parameterInformationDictionary))
	
	if(returnParameters == True):
		return parameterInformationDictionary
	else:
		return replaceMultipleStringsWithMultipleStrings(stringToReturn, parameterInformationDictionary)

def theThingsToEvaluate():
	return [
		#removeParentheses("((foo [bar]) = baz)","foo,bar"),
		#removeParentheses("((foo[bar]) = baz)","foo,bar,baz"),
		[["(foo in bar is between goo and gar)", "(foo is between goo and gar in bar)"], "foo,bar,goo,gar", "(foo in bar is between goo and gar)"],
		[["(function named funcName that returns typeToReturn with parameters named paramNames with the parameter types paramTypes theBody)", "(public static typeToReturn funcName paramNames paramTypes theBody)"], "typeToReturn,funcName,paramNames,paramTypes,theBody", "function(parameterNames=paramNames, parameterTypes=paramTypes, isStatic=True, returnType='typeToReturn', functionName='funcName', body=theBody),"],
		[["(def funcName paramNames theBody)"], "funcName,paramNames,theBody", "function(parameterNames=paramNames, parameterTypes=paramNames, isStatic=True, returnType='void', functionName='funcName', body=theBody),"],
		[["(foo = bar)"], "foo,bar", "setVar(valueToGet=bar, valueToChange=foo)"],
		[["(not foo)"], "foo", "Not(foo)"],
		[["(convert foo from bar to baz)", "(convert foo to baz from bar)", "(foo converted from baz to bar)"], "foo,bar,baz", "convert foo from bar to baz"],
		[["(cond foo)"], "foo", "conditionalBlock(foo)"],
		[["(for theInitializer theCondition theIncrement theBody)"], "theInitializer,theCondition,theIncrement,theBody", "forLoop(body=theBody, initializer=theInitializer, condition=theCondition, increment=theIncrement)"],
		[["(foo ;)"], "foo", "seriesOfStatements([foo])"],
		[["([aVar])", "(aVar,)"], "aVar", "[aVar]"],
		[["(main foo)"], "foo", "main(foo)"],
		[["(convert foo from base bar to base baz)", "(convert foo to base baz from base bar)", "(foo converted to base baz from base bar)", "(foo converted from base bar to base baz)", "(foo in base baz instead of base bar)"], "foo,bar,baz", "(convert foo from base bar to base baz)"],
		[["(foo [ bar ])"], "foo,bar", "foo[bar]"],
		[["(switch foo)"], "foo", "Switch(foo, [])"],
		[["(if foo)"], "foo", "If(foo, [])"],
		[["(while foo)"], "foo", "While(foo, [])"],
		[["(module foo)"], "foo", "module([foo])"],
		[["(default foo)"], "foo", "default(foo)"],
		[["(foo{ bar })"], "foo,bar", "foo(bar)"],
		[["(type [ dimensions ] varName = initialValue)", "(type varName [ dimensions ] = initialValue)"], "type,varName,dimensions,initialValue", "typedimensions varName = initialValue"],
		[["(theArr[ indices ])"], "theArr,indices", "theArrindices"],
		[["(type foo = bar)"], "type,foo,bar", "initializeVar(variableName=foo, variableType=type, initialValue=bar, arrayDimensions=None)"],
		[["(switch condition insideBrackets afterBrackets)"], "condition,insideBrackets,afterBrackets", "switch(condition){insideBrackets} afterBrackets"],
		[["(if condition insideBrackets afterBrackets)"], "condition,insideBrackets,afterBrackets", "If(condition, [insideBrackets]), afterBrackets"],
		[["(foo is a prime number)"], "foo", "is_prime(foo)"],
		[["(the type of foo)"], "foo", "type(foo)"],
		[["(foo divided by bar)", "(the quotient of foo and bar)"], "foo,bar", "(foo/bar)"],
		[["(foo is between bar and baz)"], "foo,bar,baz", "((bar < foo) and (foo < baz))"],
		[["(foo contains bar)", "(bar is in foo)"], "foo,bar", "(bar in foo)"],
		[["(length of foo)"], "foo", "len(foo)"],
		[["(random number between foo and bar)"], "foo,bar", "randint(foo,bar)"],
		[["(print foo)"], "foo", "puts(foo)"],
		[["(foo to the power of bar)"], "foo,bar","(foo**bar)"],
		[["(foo and bar)"], "foo,bar","(foo and bar)"],
		[["(sum of each number in foo)"], "foo","sumOfAllNums(foo)"],
		[["(return foo)"], "foo","return foo"],
		[["(foo matches bar)"], "foo,bar","re.compile(bar).matches(foo)"],
		[["(foo equals bar)", "(foo and bar are equal)"], "foo,bar", "Equals(foo, bar)"],
		[["(foo if bar)", "(if bar foo)", "(if bar then foo)"], "foo,bar", "If(bar, foo)"],
		[["(while bar foo)", "(foo while bar)"], "foo,bar", "While(bar, foo)"],
		[["(foo is divisible by bar)", "(foo is a multiple of bar)"], "foo,bar", "(foo % bar == 0)"],
		[["(foo > bar)"], "foo,bar", "greaterThan(foo, bar)"],
		[["(foo is less than bar)"], "foo,bar", "lessThan(foo, bar)"],
		[["(foo overlaps with bar)"], "foo,bar", "rangesOverlap(foo, bar)"],
		[["(replace each foo in bar with baz)"], "foo,bar,baz", "bar.replace(foo,baz)"],
		[["(else foo)"], "foo", "Else([foo]),"],
		[["(case foo bar)"], "foo,bar", "case(foo, bar)"],
		[["(switch foo bar)"], "foo,bar", "switch(foo, bar)"],
		[["(elif foo bar)"], "foo,bar", "Elif(foo, bar)"],
		[["(elif foo bar baz)"], "foo,bar,baz", "Elif(foo, bar), baz"],
		[["(foo mod bar)"], "foo,bar", "mod(foo, bar)"],
		[["(class [[foo]] [[body]])"], "[[foo]],[[body]]", "getClass([[foo]], [[body]])"],
		[["(foo / bar)"], "foo,bar", "divide(foo, bar)"],
		[["(foo has the same meaning as bar)"], "foo,bar", "foo has the same meaning as bar"],
		[["(the value of foo)"], "foo", "foo"],
		[["(test the exec function)"], '', "exec(\"print('toPrint')\")"],
	]

thingsToEvaluate = []
def evaluateMacro(stringToEvaluate, returnParameterNames=False):
	if(stringToEvaluate.startswith("exec(")):
		exec(stringToEvaluate)
		return ""
	#print("Macro to evaluate: " + str(stringToEvaluate))
	if(returnParameterNames == False):
		#print(getParameterNames(stringToEvaluate))
		pass
	global thingsToEvaluate
	if (thingsToEvaluate == []):
		thingsToEvaluate = theThingsToEvaluate()
		#print(thingsToEvaluate)
		addThingsToEvaluate = [
		removeParentheses("(foo = (bar [ baz ]))"),
		[["(unless foo bar)", "(foo unless bar)"], "(if (not foo) then bar)"],
		[["(foo squared)"], "(foo to the power of 2)"],
		[["(foo cubed)"], "(foo to the power of 3)"],
		[["(square root of foo)"], "(foo to the power of -2)"],
		[["(foo += bar)"], "(foo = (foo + bar))"],
		[["(foo *= bar)"], "(foo = (foo * bar))"],
		[["(foo -= bar)"], "(foo = (foo - bar))"],
		[["(foo /= bar)"], "(foo = (foo / bar))"],
		[["(foo ++)"], "(foo += 1)"],
		[["(foo != bar)"], "(not (foo == bar))"],
		[["(foo = foo + bar)"], "(foo += bar)"],
		[["(foo = foo - bar)"], "(foo -= bar)"],
		[["(foo = foo * bar)"], "(foo *= bar)"],
		[["(foo if bar unless baz)"], "(foo if (bar and (not baz)))"],
		[["(print the type of foofoo)"], "(print (the type of foofoo)))"],
		[["(foo percent of bar)"], "(foo * 0.01 * bar)"],
		]
		for current in addThingsToEvaluate:
			print(thingsToEvaluate[len(thingsToEvaluate)-1])
			thingsToEvaluate += [[current[0], getParameterNames(current[1]), evaluateMacro(current[1])]]
	stringToEvaluate = addParentheses(stringToEvaluate)	
	#print("String to evaluate with added parentheses:\n" + stringToEvaluate)
	#stringToEvaluate = addOpeningAndClosingParentheses(stringToEvaluate)
	#print("Evaluate the macro " + stringToEvaluate)
	#print(splitMacroWithWhitespace(stringToEvaluate))
	theArr = printMatches(replaceParenthesesWithSymbols(stringToEvaluate));
	#theData = OneOrMore(nestedExpr()).parseString(stringToEvaluate)
	#print(theData)
	whitespaceSplitString = splitMacroWithWhitespace(stringToEvaluate);
	#print("The string split with whitespace is " + str(whitespaceSplitString))
	separatorCharacter = whitespaceSplitString[1]
	if(everyOtherIsTheSame(whitespaceSplitString)):
		#print("Every other character in " + str(whitespaceSplitString) + " is " + str(separatorCharacter))
		
		nonSeparatorParts = getNonSeparatorParts(stringToEvaluate)
		
		if returnParameterNames == True:
			thingToReturn = {}
			for idx,current in enumerate(nonSeparatorParts):
				thingToReturn[idx] = current
			return thingToReturn
		
		#print("The non-separator parts are " + str(nonSeparatorParts))
		
		
		for idx, current in enumerate(nonSeparatorParts):
			if(current.startswith("(")):
				print(current)
				nonSeparatorParts[idx] = evaluateMacro(current)
		if(separatorCharacter in ["+", "plus"]):
			return "add([" + ", ".join(nonSeparatorParts) + "])"
		elif(separatorCharacter in ["-", "minus"]):
			return "subtract([" + ", ".join(nonSeparatorParts) + "])"
		elif(separatorCharacter in ["*", "times"]):
			return "multiply([" + ", ".join(nonSeparatorParts) + "])" 
		elif(separatorCharacter in ["||", "or", "|"]):
			return "Or([" + ", ".join(nonSeparatorParts) + "])"
		elif(separatorCharacter in ["and", "&&", "&"]):
			return "And([" + ", ".join(nonSeparatorParts) + "])"
		elif(separatorCharacter in [","]):
			return "[" + ", ".join(nonSeparatorParts) + "]" 
		elif(separatorCharacter in [";"]):
			return "seriesOfStatements([" + ", ".join(nonSeparatorParts) + "])"
		
	#print("String to evaluate: " + stringToEvaluate)
	#print(getMatchingRegex(stringToEvaluate))
	
	
	
	#This code does not do
	#if returnParameterNames == False:
		#if(getMatchingRegex("(foo has the same meaning as bar)") == getMatchingRegex(stringToEvaluate)):
			#print("The input is a syntax definition: " + stringToEvaluate)
			#thingToChange = evaluateMacro(stringToEvaluate, returnParameterNames=True);
			#print(thingToChange)
			#print(thingToChange['foo'])
			#print(thingToChange['bar'])
			#thingsToEvaluate += [[thingToChange['foo'], getParameterNames(thingToChange['bar']), evaluateMacro(thingToChange['bar'])]]
			#print(thingsToEvaluate)
	
	
	#else:
		#print(str(whitespaceSplitString) + " is not an arithmetic expression.")
	
	for current in thingsToEvaluate:
		for currentInputString in current[0]:
			if returnParameterNames == True:
				theResult = evaluateMacroWithSpecificString(inputString=stringToEvaluate,stringThatMatchesRegex=currentInputString,variableNames=current[1],stringToReturn=current[2], returnParameters = True)
			else:
				theResult = evaluateMacroWithSpecificString(stringToEvaluate, currentInputString, current[1], current[2])
			if(theResult != None):
				if(type(theResult) == str and theResult.startswith("exec(")):
					exec(theResult)
					return ""
				else:
					return theResult
			
	if(len(theArr) == 1):
		matchingRegex = theArr[0]["matchingRegex"]
		'''
		paramArray = splitMacroWithParentheses(stringToEvaluate)
		
		#Evaluate these before the macro has been evaluated:
		if matchingRegex == getMatchingRegex("(foo and bar are equal)"):
			return evaluateMacro("(" + paramArray[0] + " equals " + paramArray[2] + ")")
		elif matchingRegex == getMatchingRegex("(shuffle foo randomly)"):
			return evaluateMacro("(randomly shuffle " + paramArray[1] + ")")
		#Evaluate these after the macro has been evaluated
		for idx, current in enumerate(paramArray):
			if(current.startswith("(") and current.endswith(")")):
				paramArray[idx] = evaluateMacro(current)
		"(foo is divisible by bar)"
			"(foo % bar == 0)"
		"(randomly shuffle foo)"
			"my_shuffle(foo)"
		"(foo in reverse order)"
			"foo[::-1]"
		"(sort foo in alphabetical order)"
			"sorted(foo)"
		"(the type of foo)"
			"type(foo)"
		"(sort foo from largest to smallest)"
			"sorted(foo)"
		"(sort foo from smallest to largest)"
			"sorted(foo).reverse()"
		"(foo is an integer)"
			"(type(foo) == int)"
		"(all locations of foo in bar)"
			"[i for i, x in enumerate(bar) if x == foo]"
		"(pick random from foo)"
			"choice(foo)"
		"(dimensions of foo)"
			"arrayDimensions(foo)"
		"(print foo)"
			"(puts(foo))"
		"(foo from bar to baz)"
			"(substring of foo between bar and baz)"
		"(foo and bar)"
			"(foo and bar)"
		"(sum of each number in foo)"):
			"sumOfAllNums(foo)"
		"(return foo)"
			"Return(foo),"
		if(toReturn != ""
			#print(stringToEvaluate + " becomes (" + toReturn + ") which evaluates to " + str(eval(toReturn)))
			#stringToReturn = str(eval(toReturn))
			#print(stringToEvaluate + " becomes \n     " + toReturn + "\n")
			return toReturn
		else:
		'''
		raise Exception(stringToEvaluate + " matches " + matchingRegex.pattern + ", but the output is not yet defined in evaluateMacro")
		
	elif(len(theArr) == 0):
		raise Exception(replaceParenthesesWithSymbols(stringToEvaluate) + " does not match any regular expression.")
	else:
		print(stringToEvaluate) + " matches more than one regular expression!"

def printMacroOutputs(theStrings):
	for current in theStrings:
		print("To evaluate: " + current)
		print(str(current) + "\nbecomes\n    " + str(evaluateMacro(current))+"\n")


"function name: evaluateMacroWithSpecificString(inputString,variableNames,stringToReturn)"
"requires functions: splitMacroWithParentheses, replaceParenthesesWithSymbols(theString), replaceMultipleStringsWithMultipleStrings, getDictionaryFromMacro(theVariables,theMacro,theResult)"
"is defined: True"
"description: Return the output of the macro. Replace the variables in stringToReturn with the parameters"
def evaluateMacroWithSpecificString(inputString,stringThatMatchesRegex,variableNames,stringToReturn, returnParameters = False):
	#print("Input string: " + inputString)
	#print("String that matches regex: " + stringThatMatchesRegex)
	#print("variable names: " + variableNames)
	#print("string to return: " + stringToReturn)
	#Return None if the input doesn't match a regex.
	if(printMatches(replaceParenthesesWithSymbols(inputString)) == []):
		return None
	if(printMatches(replaceParenthesesWithSymbols(stringThatMatchesRegex)) == []):
		#raise Exception(stringThatMatchesRegex + " does not match any regular expression.")
		return None
	if(getMatchingRegex(replaceParenthesesWithSymbols(stringThatMatchesRegex))) != getMatchingRegex(replaceParenthesesWithSymbols(inputString)):
		return None
	
	if(variableNames == ""):
		return stringToReturn
	
	#print(replaceParenthesesWithSymbols(inputString))
	#print(getExpressionsInParentheses(inputString))
	theSplitInputString = splitMacroWithParentheses(inputString)
	theSplitParameterString = splitMacroWithParentheses(stringThatMatchesRegex)
	
	
	arrayOfVariables = variableNames.split(",")
	
	#print("theSplitInputString: " + str(theSplitInputString))
	#print("theSplitParameterString: " + str(theSplitParameterString))
	#print("theSplitStringToReturn: " + str(theSplitStringToReturn))
	#print("arrayOfVariables: " + str(arrayOfVariables))
	
	parameterInformationDictionary = {}
	
	#The location of each variable in theSplitInputString is the same as the location of each variable in the
	
	if returnParameters == False:
		for idx, current in enumerate(theSplitInputString):
			if current.startswith("(") and current.endswith(")"):
				#print("Thing to evaluate: " + current)
				theSplitInputString[idx] = evaluateMacro(current)
	
	for current in arrayOfVariables:
		for idx, current1 in enumerate(theSplitParameterString):
			#print(current + ", " + current1)
			if current1 in current:
				parameterInformationDictionary[current] = theSplitInputString[idx]
	
	#print("parameterInformationDictionary: " + str(parameterInformationDictionary))
	
	if(returnParameters == True):
		return parameterInformationDictionary
	else:
		return replaceMultipleStringsWithMultipleStrings(stringToReturn, parameterInformationDictionary)
	
	'''
	
	Return the string that is to be evaluated.
	
	evaluateMacroWithSpecificString("(3 == (4+1))", ["(foo equals bar)"], "foo,bar", "(foo == bar)")
	
	First, get a dictionary to represent the indices of all parameters in the 
	
	Then, get a list of all regular expressions that match the input string.
	
	Ensure that each string in stringsThatMatchRegexes matches one regex, and each regex in stringsThatMatchRegexes matches one string.
	
	'''
#print(evaluateMacroWithSpecificString("(3 == (4 plus 1))", "(foo equals bar)", "foo,bar", "(foo == bar)"))

#print(evaluateMacro("(5 is between (4 times 4) and 7)"))
#print(evaluateMacro("([1,2,3,4] contains 4)"))

def getParameterNames(theMacro):
	thingToChange = evaluateMacro(theMacro, returnParameterNames=True);
	#print("ThingToChange is " + str(thingToChange))
	thingToChange1 = thingToChange.keys()
	thingToReturn = []
	for idx,current in enumerate(thingToChange1):
		thingToReturn += [thingToChange[thingToChange1[idx]]]
	for idx, current in enumerate(thingToReturn):
		if current.startswith("("):
			thingToReturn[idx] = getParameterNames(current)
	print(thingToReturn)
	thingToReturn = ",".join(thingToReturn)
	thingToReturn = thingToReturn.split(",")
	return ",".join(list(set(thingToReturn)))

print(getMatchingRegex("(print 1)"))
print(getMatchingRegex("(print the type of 1)"))
print(getParameterNames("(baz is between barf and frog)"))
print(evaluateMacro("(gorf cubed)"))
print(evaluateMacro("(gorf squared)"))
print(evaluateMacro("(test the exec function)"))
print(evaluateMacro("exec(\"print('derp')\")"))
