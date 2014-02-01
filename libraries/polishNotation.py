#The new version is in polishNotation2.py. Use that version instead of using this version.







#To do:
	#Find out how to split a string using matches of a regular expression as the separator.

#Test everything in polyglotCodeGenerator.py

#Use re.match(expr, stringToSplit).groups() to split a string with its parameters:
#http://stackoverflow.com/questions/18903923/how-to-split-a-string-in-python-without-redundant-output

from pyparsing import OneOrMore, nestedExpr
import re

def splitParameterString(theString):
	toFilter = re.compile("(<<(?:[^\s]+)>>)").split(theString)
	return filter(lambda a: a != '', toFilter)

def getRegexFromString(theString):
	theSplitString = splitParameterString(theString)
	for x in range(0, len(theSplitString)):
		if theSplitString[x].startswith("<<") and theSplitString[x].endswith(">>"):
			theSplitString[x] = "([^\s]+)"
	return re.compile("".join(theSplitString))

def splitStatement(theRegex, stringToSplit):
	return re.match(theRegex, stringToSplit).groups()

def getThingToCheckAgainstRegex(theArray):
	theCounter = 0
	toReturn = ""
	for idx, current in enumerate(theArray):
		if(idx != 0):
			toReturn += " "
		if (type(current) != str or (type(current) == str) and (("'" in current) or ('"' in current))):
			theCounter += 1
			toReturn += "<<" + str(theCounter) + ">>"
		else:
			toReturn += current
	return toReturn

stringToTest = "(replace(?: each| every|)) <<foo>> (in|inside(?: of)|within) <<bar>> (with) <<baz>>"
theRegex = getRegexFromString(stringToTest)
print(splitParameterString(stringToTest))
print(splitStatement(theRegex, "replace (a) in b with c"))
print(splitStatement(theRegex, "replace a within b with c"))
print(splitStatement(theRegex, "replace a inside of b with c"))
print(splitStatement(theRegex, "replace every a in b with c"))

#I'm still working on crossLanguageParser.py, but I'm trying to see if I can get this new syntax to work.
#This is supposed to be a re-write of crossLanguageParser.py, using Polish notation.

#evaluateMacro is the main function here.

#print(getThingToCheckAgainstRegex(["the", "type", "of", ["foo", "goo"], "is", "'bar'"]))

def isParameter(theString):
	if theString.startswith("<<") and theString.endswith(">>"):
		return True

arrayOfOutputs = [

[["<<type>>  [ <<dimensions>> ] <<name>> = <<initialValue>>", "<<type>> <<name>> [ <<dimensions>> ] = <<initialValue>>"], "initializeVar('<<name>>', '<<type>>', <<initialValue>>, <<dimensions>>)", "final"],

[["<<type>> <<name>> = <<initialValue>>"], "(<<type>>  [ None ] <<name>> = <<initialValue>>)"],

#def initializeVar(variableName, variableType, initialValue, arrayDimensions):

[["def <<isStatic>> <<returnType>> <<functionName>> <<parameterNames>> <<parameterTypes>> <<body>>"], "getFunction('<<functionName>>', '<<isStatic>>', <<parameterNames>>, <<parameterTypes>>, '<<returnType>>', <<body>>)", "final"],

[["return <<toReturn>>",], "Return(<<toReturn>>)", "final"],
[["while <<condition>> <<action>>"], "whileLoop([<<action>>], <<condition>>)", "final"],
[["switch <<condition>> <<action>>",], "switch(<<condition>>, [<<action>>])", "final"],
[["case <<condition>> <<action>>"], "case(<<condition>>, [<<action>>])", "final"],


[["else <<action>>", "else { <<action>> }"], "Else([<<action>>])", "final"],
[["if <<condition>> then <<output>>", "<<output>> unless <<condition>> is false", "if <<condition>> { <<output>> }", "<<output>> if <<condition>>", "<<output>> if and only if <<condition>>", "if <<condition>> <<output>>"], "If(<<condition>>, [<<output>>])", "final"],
[["elif <<condition>> <<action>>", "else if <<condition>> then <<action>>"], "Elif(<<condition>>, [<<action>>])", "final"],

[["<<param1>> ; <<param2>>", "<<param1>> , <<param2>>"], "<<param1>>,<<param2>>", "final"],
[["<<param1>> ;", "<<param1>> ,"], "<<param1>>,", "final"],

[["module <<body>>"], "module([<<body>>])", "final"],
[["main <<body>>"], "main([<<body>>])", "final"],
[["<<value1>> == <<value2>>", "<<value1>> is <<value2>>", "<<value1>> equals <<value2>>", "<<value1>> is equal to <<value2>>"], "equals(<<value1>>, <<value2>>, 'int')", "final"],
[["<<item>> is in <<array>>", "<<array>> contains <<item>>"], "(<<item>> in <<array>>)", "final"],
#If it ends in "final", then the output string is directly returned.
[["not <<x>>", "! <<x>>"], "Not(<<x>>)", "final"],
[["replace each <<contained>> in <<container>> with <<replacement>>", "replace every <<contained>> in <<container>> with <<replacement>>"], "replace each <<contained>> in <<container>> with <<replacement>>", "final"],
#If there are only 3 items in the array, then the output is translated into another macro
[["unless <<condition>> <<action>>", "<<action>> unless <<condition>>"], "(if (not <<condition>>) then <<action>>)"],
[["while <<condition>> <<action>>", "<<action>> while <<condition>>", "do <<action>> while <<condition>> is true", "<<action>> until <<condition>> becomes false"], "while(<<condition>>){<<action>>}", "final"],
#"eval" means the output string will be directly evaluated.
[["<<thing1>> means <<thing2>>"], "addToArray(<<thing1>>, <<thing2>>)", "eval"],
[["<<functionName>> { <<parameterList>> }"], "callFunction('<<functionName>>', None, [<<parameterList>>])", "final"],
[["<<param1>> + <<param2>>", "<<param1>> plus <<param2>>"], "add([<<param1>>, <<param2>>])", "final"],
[["<<param1>> - <<param2>>"], "subtract(<<param1>>, <<param2>>)", "final"],
[["<<param1>> * <<param2>>"], "multiply(<<param1>>, <<param2>>)", "final"],
[["<<param1>> / <<param2>>", "<<param1>> divided by <<param2>>"], "divide(<<param1>>, <<param2>>)", "final"],
[["<<param1>> % <<param2>>"], "Mod([<<param1>>, <<param2>>])", "final"],
[["<<param1>> or <<param2>>", "<<param1>> || <<param2>>"], "Or(<<param1>>, <<param2>>)", "final"],
[["<<param1>> > <<param2>>", "<<param1>> is greater than <<param2>>"], "greaterThan(<<param1>>, <<param2>>)", "final"],
[["<<param1>> < <<param2>>", "<<param1>> is less than <<param2>>>>"], "lessThan(<<param1>>, <<param2>>)", "final"],
[["<<param1>> <= <<param2>>"], "lessThanOrEqualTo(<<param1>>, <<param2>>)", "final"],
[["<<param1>> >= <<param2>>"], "greaterThanOrEqualTo(<<param1>>, <<param2>>)", "final"],
[["<<param1>> and <<param2>>", "<<param1>> && <<param2>>" "<<param1>> & <<param2>>"], "And(<<param1>>, <<param2>>)", "final"],

[["class <<className>> { <<body>> }",], "getClass(<<className>>, <<body>>)", "final"],
#def getClass(className, body):

[["<<param>> ++"], "(<<param>> += 1)"],
[["<<param>> --"], "(<<param>> -= 1)"],

[["seriesOfStatements <<param>>", "series of statements <<param>>"], "seriesOfStatements([<<param>>])", "final"],

[["<<param1>> += <<param2>>"], "(<<param1>> = (<<param1>> + <<param2>>))"],
[["<<param1>> -= <<param2>>"], "(<<param1>> = (<<param1>> - <<param2>>))"],
[["<<param1>> *= <<param2>>"], "(<<param1>> = (<<param1>> * <<param2>>))"],
[["<<param1>> ^= <<param2>>"], "(<<param1>> = (<<param1>> ^ <<param2>>))"],


[["<<param1>> = <<param2>>"], "setVar(<<param2>>, <<param1>>)", "final"],
#def setVar(valueToGet, valueToChange):

[["for <<initializer>> <<condition>> <<increment>> <<action>>", "for <<initializer>> ; <<condition>> ; <<increment>> { <<action>> }"], "forLoop(<<action>>, <<initializer>>, <<condition>>, <<increment>>)", "final"],
#def forLoop(body, initializer, condition, increment):

[["for <<variable>> from <<start>> to <<end>> <<action>>"], "(for [ (<<variable>> = <<start>>) ; (<<variable>> < <<end>>) ; (<<variable>> ++) ] { <<action>> })"],
[["<<param1>> ^ <<param2>>", "<<param1>> to the power of <<param2>>", "param1 ** param2"], "<<param1>>^<<param2>>", "final"],
[["[ <<param>> ]"], "[<<param>>]", "final"],
[["<<className>> . <<methodName>> { <<methodParameters>> }"], "<<className>>.<<methodName>>(<<methodParameters>>)", "final"]


]
	
def addToArray(thing1, thing2):
	global arrayOfOutputs
	thing2 = ("(" + thing2 + ")")
	thing2 = list(OneOrMore(nestedExpr()).parseString(thing2)[0])
	thing1 = thing1.split(" ")
	arrayOfOutputs += [[thing1, thing2]]

for idx1, current1 in enumerate(arrayOfOutputs):
	currentStringOutput = current1[1]
	for idx2, current2 in enumerate(current1[0]):
		current1[0][idx2] = current1[0][idx2].split(" ")
	if(len(current1) == 2):
		current1[1] = OneOrMore(nestedExpr()).parseString(currentStringOutput)[0]

#print(arrayOfOutputs)

def compareStringLists(listWithParameters, listDefiningThePattern):
	if(len(listWithParameters) != len(listDefiningThePattern)):
		return False
	for idx, current in enumerate(listWithParameters):
		if(not isParameter(listDefiningThePattern[idx])):
			if(not (listWithParameters[idx] == listDefiningThePattern[idx])):
				return False
	return True
	
def replaceInMultiDimensionalArray(theArray, toReplace, newReplace):
	for idx, current in enumerate(theArray):
		if current == toReplace:
			theArray[idx] = newReplace
		if type(current) != str:
			theArray[idx] = replaceInMultiDimensionalArray(current, toReplace, newReplace)
	return theArray
	
#print(replaceInMultiDimensionalArray(['hello', 'dude', ['lol', 'lol', 'hello', ['woo', 'hello', 'woo']]], 'hello', 'hoohoo'))

#print(getRegexStringFromArray(["Hi", ["lol", 1, 2, "what is this"]]))

def putInsideArray(theArray, startingIndex, endingIndex):
	theSubArray = theArray[startingIndex:(endingIndex+1)]
	theArray[startingIndex:endingIndex] = []
	theArray[startingIndex] = theSubArray
	return theArray

#print(putInsideArray([1,3,3,4,5], 1, 3))

#requires putInsideArray and compareStringLists
#This surrounds the last match of the pattern with parentheses.
def putPatternInsideArray(theArray, thePattern):
	for current in reversed(range(0,len(theArray))):
		theTestArray = theArray[current:(current+len(thePattern))]
		if(compareStringLists(theTestArray, thePattern) == True):
			return putInsideArray(theArray, current, current+len(thePattern)-1)
			
#print(putPatternInsideArray(["hello", "hello", ["woop", "woop"]], ["hello", "<<derp>>"]))

#print(range(0, 5))

arrayToCheck = ["lol", "wut", "hello", "world", "lol"]
#print(putPatternInsideArray(arrayToCheck, ["hello", "world"]))
#print(putPatternInsideArray(arrayToCheck, ["wut", "<<testingThing>>", "lol"]))

def putFirstPatternInsideArray(theArray, thePatterns):
	firstLength = len(theArray)
	for current in thePatterns:
		putPatternInsideArray(theArray, current)
		if(len(theArray) != firstLength):
			return theArray

def putEveryPatternInsideArray(theArray):
	arrayOfPatterns = []
	for current in arrayOfOutputs:
		arrayOfPatterns += current[0]
	arrayOfPatterns.sort(key=len)
	arrayOfPatterns = arrayOfPatterns[::-1]
	#print(arrayOfPatterns)
	while True:
		oldArrayLength = len(theArray)
		putFirstPatternInsideArray(theArray, arrayOfPatterns)
		if(len(theArray) == oldArrayLength):
			break;
	if(len(theArray) == 1):
		return theArray[0]
	else:
		return theArray

putEveryPatternInsideArray(["hi", "lol"])


def evaluateMacro(theList):
	theList = list(theList)
	theList = putEveryPatternInsideArray(theList)
	#print(theList)
	if (len(theList) == 1):
		return evaluateMacro(theList[0])
	#print regexString
	for idx, currentOutputArray in enumerate(arrayOfOutputs):
		currentOutputString = currentOutputArray[1]
		currentSplitStringList = currentOutputArray[0]
		for idx1, currentSplitStringList1 in enumerate(currentSplitStringList):
			if(compareStringLists(theList, currentSplitStringList1)):
				currentSplitStringList = currentSplitStringList[idx1]
				toReturn = currentOutputString
				if((len(currentOutputArray) == 3)):
					for idx2, currentParameter in enumerate(theList):
						if type(currentParameter) != str:
							theList[idx2] = evaluateMacro(currentParameter)
						if isParameter(currentSplitStringList[idx2]):
							toReturn = toReturn.replace(currentSplitStringList[idx2], theList[idx2])
					if currentOutputArray[2] == "final":
						return toReturn
					elif currentOutputArray[2] == "eval":
						exec toReturn;
						return ""
				else:
					for idx2, currentParameter in enumerate(theList):
						if isParameter(currentSplitStringList[idx2]):
							toReturn = replaceInMultiDimensionalArray(toReturn, currentSplitStringList[idx2], currentParameter)
					#print(toReturn)
					return evaluateMacro(toReturn)	
	raise Exception(str(theList) + " does not match any pattern.")
		
#evaluateMacro(OneOrMore(nestedExpr()).parseString("('gorp <<toPrint>>' means 'print <<toPrint>>')")[0])
#evaluateMacro(OneOrMore(nestedExpr()).parseString("('<<action>> unless <<condition>>' means 'if (not <<condition>>) then <<action>>')")[0])
#print("The output is " + evaluateMacro(OneOrMore(nestedExpr()).parseString("(gorp 1)")[0]))
#print(arrayOfOutputs[len(arrayOfOutputs) - 1])
#print(arrayOfOutputs[4])

def printOutput(theInput):
	print("The output of "+theInput+" is " + evaluateMacro(OneOrMore(nestedExpr()).parseString(theInput)[0]))

def getStringOutput(theInput):
	return evaluateMacro(OneOrMore(nestedExpr()).parseString("(" + theInput + ")")[0])

#printOutput("(x is in arr1)")
#printOutput("(arr1 contains 'a string')")
#printOutput("(if (x equals true) then (print { goodbye }) (else print { hello }))")
#printOutput(
'''
(

(if (x == 3)
	(print { x + 1 })
	(else if (x == 4) then
		(print { x ^ 5 })
		(else
			print { x + 3 + 4 }
		)
	)
)

)
'''#)
#printOutput("(foo { ([ 3 , 4 , 5 , 6 , 5 , 4 ]) })")
#printOutput("(print { sum { product { lol * derp } } })")
#printOutput(
'''
((print { x }) if and only if
	(x is true)
	(else
		print { hello }
	)
)
'''
#)
#printOutput("([ 1 , ([ 2 , 7 , 9 ]), 3 ])")
#printOutput("(function paramNames paramTypes (return 3))")
#printOutput("(class HelloWorld { print { hello } })")
#printOutput("(foo plus bar plus baz)")
#printOutput("(foo < bar < baz)")
#printOutput("(foo is greater than bar)")
#printOutput("(foo >= bar >= baz)")
#printOutput("(foo <= bar <= baz)")
#printOutput("(foo ++)")
#printOutput("(foo --)")
#printOutput("(foo to the power of 3)")
#printOutput("([ 1 , ([ 1 , 2 , 3 , ([ lol , derp , hee , hoo ]) ]) , 1 ])")
#printOutput(
'''
	(for (i = 0) ; (i < 10) ; (i ++) {
			(print { i }) 
	})
'''
#)
#printOutput(
'''
	(for i from 1 to 10 {
			(print { i } ; print { (i + 1) } ; print { (i to the power of 2) } ;)
	})
'''
#)
#printOutput("(lol . derp { hi })")
#printOutput(
'''(
main
	print { hello } ; print { derp } ; print { i + 1 + 3 } ;
)'''#)

#semicolon(semicolon(print(hello)), semicolon(print(derp)), print(add(i, add(1, 3))))
