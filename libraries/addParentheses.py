from cfor import cfor
from copy import copy

def numberOfIndentations(theString):
	if(theString.strip() == "" or theString == None):
		return 0
	counter = 0
	for current in theString:
		if current == "	":
			counter += 1
		else:
			return counter

def addInitialParentheses(theString, previousIndentation, nextIndentation):
	#previousIndentation is the previous number of indentation and nextIndentation is the next number of indentations
	pass

def addFinalParentheses(theString, previousIndentation, nextIndentation):
	#previousIndentation is the previous number of indentation and nextIndentation is the next number of indentations
	pass

def addSemicolons(theString):
	#print(theString)
	theStrings = theString.split("\n")
	theNewStrings = copy(theStrings)
	#print(theNewStrings)
	for i in range(0, len(theStrings)):
		previousIndentation = 0
		currentIndentation = numberOfIndentations(theStrings[i])
		nextIndentation = numberOfIndentations(theStrings[i])
		if(i == 0):
			previousIndentation = 0
		else:
			previousIndentation = numberOfIndentations(theStrings[i-1])
		if(i == (len(theStrings) - 1)):
			nextIndentation = 0
		else:
			nextIndentation = numberOfIndentations(theStrings[i+1])
		if ((nextIndentation <= currentIndentation) and not theNewStrings[i].endswith(";") and theNewStrings[i].strip() != ""):
			theNewStrings[i] = theNewStrings[i] + ";"
	#theNewStrings = filter(None, theNewStrings)
	#print(theNewStrings)
	#print("\n".join(theNewStrings))
	return "\n".join(theNewStrings)

def addParentheses(theString):
	#theString = addSemicolons(theString)
	theStrings = theString.split("\n")
	theNewStrings = copy(theStrings)
	for i in range(0, len(theStrings)):
		previousIndentation = 0
		currentIndentation = numberOfIndentations(theStrings[i])
		nextIndentation = numberOfIndentations(theStrings[i])
		if(i == 0):
			previousIndentation = 0
		else:
			previousIndentation = numberOfIndentations(theStrings[i-1])
			
		if(i == (len(theStrings) - 1)):
			nextIndentation = 0
		else:
			nextIndentation = numberOfIndentations(theStrings[i+1])
			
		#print("\nPrevious indentation: " + str(previousIndentation))
		#print("Current indentation: " + str(currentIndentation))
		#print("Next indentation: " + str(nextIndentation))
		
		'''
		if ((nextIndentation <= currentIndentation) and not theNewStrings[i].endswith(";") and theNewStrings[i].strip() != ""):
			theNewStrings[i] = theNewStrings[i] + ";"
		'''
		
		if(theNewStrings[i].endswith(";")):
			theNewStrings[i] = "(" + theNewStrings[i] + ")"
		if(nextIndentation > currentIndentation):
			theNewStrings[i] = "(" + theNewStrings[i] + " ("
		if(currentIndentation < previousIndentation):
			thingToAdd = ""
			for current in range(0, (previousIndentation-currentIndentation)):
				thingToAdd += "))"
			theNewStrings[i] = thingToAdd + theNewStrings[i]	
	return "\n".join(theNewStrings)

stringToTest = '''while (x > 1)
	x -= 1;
	x -= 2;
print x; print x;

print x;
'''

print(addParentheses(
	stringToTest
))

print(addParentheses(addSemicolons(
	stringToTest
)))

if(stringToTest == addSemicolons(stringToTest)):
	print("It doesn\'t change")
