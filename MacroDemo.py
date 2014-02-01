'''
This file is no longer being used.
Use main.py instead.
'''















from __future__ import division
import numpy
import re
import math



from libraries import polishNotation2
from subprocess import call



from libraries import convertBases
convertBases = convertBases.convertBases

from libraries import syntaxRules

#pythonSyntaxRules = polishNotation2.syntaxInLanguage(syntaxRules = syntaxRules.syntaxRules, theLanguage = "Python")

#This is the main file for all of my macro language projects.

#The syntax rules for these macros are defined within syntaxRules.py in the 'libraries' folder.

#An experimental programming language translator is defined in polyglotCodeGenerator.py

#Use Pillow to generate images: http://www.pythonforbeginners.com/modules-in-python/how-to-use-pillow/

loopCondition = '5/4'

'''
def "recursively sort the array <<foo>>"
	
'''

'''
polishNotation2.testMacro("(1) to the power of (2)")
polishNotation2.testMacro("the square root of (4)")
polishNotation2.testMacro("5.4 rounded up")
polishNotation2.testMacro("5.4 rounded down")
polishNotation2.testMacro("5 / 4")
polishNotation2.testMacro("split the string 'Hello world' with the separator 'o'")
polishNotation2.testMacro("'Hello' contains 'o'")
polishNotation2.testMacro("The string 'derp' matches the regex ('(h|d)erp')")
polishNotation2.testMacro("all occurrences of 'oo' in the string 'oh woohoo hoo'")
polishNotation2.testMacro("all indices of 'hi' in the array (split the string 'hiohioohio' with the separator 'o')")
polishNotation2.testMacro("split the string 'hiohioohio' with the separator 'o'")
polishNotation2.testMacro("the dimensions of [[1,2],[3,4]]")
polishNotation2.testMacro("the regular expression 'h(o|i)' matches the string 'hi'")
polishNotation2.testMacro("insert 'hi' after the index 1 inside the array [1,2,3]")
polishNotation2.testMacro("insert 'hi' before the index 1 in the array [1,2,3]")
polishNotation2.testMacro("every integer between (1) and (5)")
polishNotation2.testMacro("join the array (split the string 'woohoohoo' with the separator 'h') with the separator ('ch')")

polishNotation2.testMacro("the regex '(?:foo)' matches the string 'foo'")

polishNotation2.testMacro("[1,2,3,4,5] written in reverse")

polishNotation2.testMacro("4 to the power of 5")

polishNotation2.testMacro("each occurrence of 4 in the list [1,2,4,2,4,3,4]")

polishNotation2.testMacro("remove every occurrence of 1 from the array [1,2,3,4,2,1,1,2,1]")
polishNotation2.testMacro("remove each occurrence of the value 1 from the array [1,2,3,4,2,1,1,2,1]")
polishNotation2.testMacro("remove each occurrence of the value 1 in the array [1,2,3,4,2,1,1,2,1]")
polishNotation2.testMacro("indices from 1 to 2 in [3,1,4,1,5,9]")
polishNotation2.testMacro("remove each occurrence of 'lol' in the string 'the lolz'")
polishNotation2.testMacro("replace every occurrence of 'the' in the string 'the lolz' with 'huh'")

polishNotation2.testMacro("every occurrence of 'l' in 'hello'")

polishNotation2.testMacro("[[1,2,2],[2,7],[4,5],[2,2]] is a 1 dimensional array")
polishNotation2.testMacro("the dimensions of [[2,2],[2,7],[4,5],[2,2]]")
polishNotation2.testMacro("the array [3,2,4,3] from 1 to 3")
polishNotation2.testMacro("[1,2,3,4] and [1,1,1,1] have the same dimensions")
#polishNotation2.testMacro("the md5 checksum of 'Hello world'")
polishNotation2.testMacro("absolute value of -3")
polishNotation2.testMacro("5 is not equal to 3")
polishNotation2.testMacro("5 does not equal 3")
polishNotation2.testMacro("'hello' does not contain 'o'")
#polishNotation2.testMacro("the array [1,2,3,4] from index 1 to index 3")
#polishNotation2.testMacro("all occurrences of 1 in the array [1,2,3,2,3,1]")
#polishNotation2.testMacro("arrange [1,2,3,4] randomly")
polishNotation2.testMacro("rotate the array [[1,0,3],[1,0,3],[1,0,3]] 90 degrees clockwise")
polishNotation2.testMacro("rotate the array [[1,0],[1,0]] 90 degrees counterclockwise")
polishNotation2.testMacro("rotate the array [[1,0],[1,0]] 180 degrees")
polishNotation2.testMacro("convert '10' from base 2 to base 10")
polishNotation2.testMacro("(print { x }) if (x == 1)")
'''

syntaxRules = syntaxRules.syntaxRules
javaSyntaxArray = polishNotation2.makeReallyNewInfoArray(syntaxRules, "Java")
pythonSyntaxArray = polishNotation2.makeReallyNewInfoArray(syntaxRules, "Python")
crossLanguageSyntaxArray = polishNotation2.makeReallyNewInfoArray(syntaxRules, "crosslanguage")

print(polishNotation2.testMacro(
'''
print{1}; print{1};
while (i < 100)
	print{i};
if (i < 10)
	print{i}; print{i};
''', crossLanguageSyntaxArray
))

print(polishNotation2.testMacro(
'''
while (i < 100)
	print{i}
if (i < 10)
	print{i}
''', pythonSyntaxArray
))



macrosToDefine = []
	
'''
def tokenizeString(theString, theTokens):
	theString = repr(theString) #string literal representation
	for i in range (0, len(theString)):
		for current in theTokens:
			print("Index " + str(i) + " with " + current + " versus " + theString[i:len(current)+i])

tokenizeString('foo("bar \'" ")', ["(", " ", "\"", "\\\"", "'", "\\'", ")"])
'''

def defMacro(theInput, theOutput):
	global syntaxRules
	global pythonSyntaxArray
	print("Calling defMacro")
	print("Define a macro with the input " + theInput + " with the output " + theOutput)
	syntaxRules += [[[theInput], theOutput]]
	pythonSyntaxArray = polishNotation2.makeReallyNewInfoArray(syntaxRules, "Python")

def testPythonMacro(theInput):
	return polishNotation2.testMacro(theInput, pythonSyntaxArray)

def makeDefinitionList(theInput):
	#This is the function that defines a series of macros.
	theInputs = theInput.split("\n")
	for current in theInputs:
		if current != "":
			exec testPythonMacro(current)

'''
makeDefinitionList( #Define new macros while modifying the syntax for the definition of new macros.

define the macro "(printing) <<derp>>" with the output "print <<derp>>"
define the macro "((?:understand|believe|interpret)(?: the macro|)) <<foo>> (to mean) <<bar>>" with the output "define the macro <<foo>> with the output <<bar>>"
understand the macro "(smorking) <<dork>>" to mean "print <<dork>>"
interpret "woof woof" to mean "print('hey')"
interpret "<<foo>> (means) <<bar>>" to mean "understand the macro <<foo>> as the macro <<bar>>"
"gorp gorp" means "print('hee!')"
understand "(now) <<foo>> (means) <<bar>>" to mean "define the macro <<foo>> with the output <<bar>>"
now "yerp yerp" means "gorp gorp"

)
'''

exec testPythonMacro(
'''

'''
)

'''
print{the next 3 letters in "hello" starting at index 1}
print{the previous 3 letters in "hello" ending at index 3}
print{100.3}
print{random number between 5 and 10}
print{generate an image from the color array [["red", "red"], ["black", "black"]] and save it as "macroImageTest.png"}
print{the color name of the rgb array [0, 0, 0]}
#print{the rgb array of the color name "black"}
'''

'''print{a random number}'''
#print(theRotatedArray)

while(loopCondition != "quit"):
	print("Enter some macros. Type 'quit' to exit.")
	print("You can also define macros here: try typing \"define the macro '(I say) <<hello>>' which means 'print <<hello>>'\"")
	loopCondition = raw_input()
	theResult = polishNotation2.testMacro(loopCondition, pythonSyntaxArray)
	print("means " + theResult + " which produces this output:")
	exec theResult

#polishNotation2.testMacro("all occurrences of the 2D array [[1,1],[2,2]] in the 2D array [[1,1,1],[2,2,2]]")

['the', 'dimensions', 'of', ['[', ['1', ',', '1', ',', '2', ',', '2'], ']'], '[', ']']
