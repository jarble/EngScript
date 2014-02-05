import re
import time
import polishNotation2

print(polishNotation2)

print(
('''
hello
derp
hi
''').split("\n")
)

print(re.split("(==|=|''')", "'derp' '''hello''' 3 == \"3\""))
#This is how to tokenize a string using a list of symbols in Python

def getMatchingRegex(theString):
	pass
	theRegexes = ['(?:regex|regular expression|regexp)', '(reversed|((?:written|spelled) (?:backwards|in reverse)))']
	regexesToReturn = []
	for current in theRegexes:
		if re.compile(current).match(theString):
			regexesToReturn += [current]
	if(len(regexesToReturn) == 1):
		return regexesToReturn[0]
	else:
		raise Exception("The regexes that match " + theString +" are "+ str(regexesToReturn))	

def fixSyntax(theString):
	if (("\\" in theString) or ("?:" in theString)):
		return theString
	else:
		for current in [".", "?", "/", "}", "]", "{", "[", "-", "+", "*", "^", "%", "$", "#", "@", "!", "~", "`"]:
			theString = theString.replace(current, "\\" + current)
		theString = theString.replace("(", "(?:")
		theString = filter(None, re.split("(\<\<[^\s]+\>\>)",theString))
		#print(theString)
		for i in range(0, len(theString)):
			current = theString[i]
			if not current.startswith("<<"):
				theString[i] = "(" + current + ")"
		#print(theString)
		theString = "".join(theString)
		#print(theString)
		return theString.replace(" )<<", ") <<").replace(">>( ", ">> (")


def makeSyntaxArrayFromString(theString):
	theArray = theString.split("\n")
	print(theArray)

print fixSyntax("<<foo>> {}")

print(fixSyntax("it is (false|(not |un)true) that <<foo>>"))
print(fixSyntax("(it is true that) <<foo>>"))

fixSyntax("<<foo>> (is between) <<bar>> and <<baz>>")
print(fixSyntax("<<foo>> (is (greater|more) than) <<bar>> ((and|but) less than) <<baz>>"))


'''
print{every match of the regular expression "(h(?:a|e)llo|halo)" in the string "hallo hello halo"}
print{the longest string in ["hello", "herp", "wha"]}
print{the longest match of the regular expression "(h(?:a|e)llo|halo)" in the string "hallo hello halo"}
'''

'''
for i in range(0, len(syntaxRules)):
	current = syntaxRules[i]
	if(len(current) == 3):
		if(type(current[1]) == dict):
			if("Python" in current[1].keys()):
				print(current[1]["Python"])
				for current1 in current[0]:
					print("	"+current1)
		else:
			print(current[1])
			for current1 in current[0]:
				print("	"+current1)
'''
def makeSyntaxRules(syntaxRules):
	for i in range (0, len(syntaxRules)):
		#print(i)
		if(type(syntaxRules[i][0]) == str):
			syntaxRules[i][0] = [syntaxRules[i][0]]
		current = syntaxRules[i]
		for j in range(0, (len(syntaxRules[i][0]))):
			syntaxRules[i][0][j] = fixSyntax(syntaxRules[i][0][j])
		#print(current)
		theOutput = current[1]
		if(type(theOutput) == str and (len(current) > 2)):
			syntaxRules[i][1] = {"Python":theOutput}
			#raise Exception("In the list " + str(current) + ", " + theOutput + " is a string, but it should be a dictionary")
	return syntaxRules

def testMacro(syntaxRules, theInput):
	syntaxRules = makeSyntaxRules(syntaxRules)
	pythonSyntaxArray = polishNotation2.makeReallyNewInfoArray(syntaxRules, "Python")
	return polishNotation2.testMacro(theInput, pythonSyntaxArray)
	pass

#syntaxRules = makeSyntaxRules(syntaxRules)
