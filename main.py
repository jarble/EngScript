print((1,2,3,4) in [1,2,3,4,5])

from libraries import syntaxRules

#import syntaxRules from libraries as herpy

import englishToPython
testMacro = syntaxRules.testMacro

def printAndTest(theString):
	theString = testMacro(englishToPython.englishToPython, theString)
	print(theString)
	exec theString

exec testMacro(englishToPython.englishToPython,
'''
import re
import numpy
import choice from random
import time
import copy
import random
import math
from libraries import syntaxRules as herpy

import pythonFunctions

print{10 cubed}
print "Demonstration of new list comprehension syntax"
print (each x inside [1,2,3,4,5,6] such that (x is divisible by 2))
#This is some EnglishScript code.

#These are EngScript's built-in Python functions.



print{the square of 2}
let goo be 1

add 3 to goo
subtract 1 from goo
multiply goo by 4
divide goo by 2
print{"goo is ", goo}


print (everything in [1,2,3,4] is in [1,2,3,4,5])
print{["Hello", "World", "Now"] contains all of these things: ["Now", "Hello"]}

#Create a string from a file
print{create a string from the file called "README.md"}

#Save a string as a file
print{save the string "Woohoo!" to a file called "ExampleText.txt"}

#Get the first few letters of a string
print{the first 3 letters of "EngScript"}
#This prints "Eng".

#print the length of a string
print{the length of "Hello World!"}

#The following two statements have exactly the same meaning.
let x be 1
x = 1

x = (the sum of x and 1)
if ((x) is not equal to (7)) :
	print x

do this 3 times:
	print "Wow!"

repeat 100 times:
	print "Hello!"

each x in  [11, 13, 16, 19] that meets this condition: (x is a prime number)

print{the greatest common factor of 25 and 100}
#print{the common factors of [10, 14, 100, 25]}

print{"Hi!"}.
make an empty file called "empty_file.txt"
print (something taken randomly from [1,2,3,4,5,6])
print{["hello", "world", "herp", "derp"] in alphabetical order}.
print{arrange ["hello", "world", "herp", "derp"] in alphabetical order}
print{["hello", "world", "herp", "derp"] arranged in alphabetical order}
print{the smallest number in [3,4,5,3,2]}
#Each of these macros are defined using makeDefinitionList.
print (the first 2 items in ["foo", "bar", "baz"])
churp = [1,[2,1],3,4,5].
print "Printing something in churp".
print{(churp[1][1]) + (churp[0])}
print{len{[1,2,3,4,5,6]} / 3}
print{split [1,2,3,4,5,6] into 3 equal parts}
print{divide "Hello!" into 3 equal parts}
#(print{"Hello"} for the next 3)
print{every foo in [3,6,9,12] meets this condition: (foo is divisible by 3)}
print{all strings in ["hello", "halo"] that match the regular expression "hello"}
print{every match of the regular expression "(h(?:a|e)llo|halo)" in the string "hallo hello halo"}
print{the longest string in ["hell", "herp", "wha"]}
print{"Longest match in string:"}.
print{longest match of the regular expression "(h(?:a|e)llo|halo)" in the string "hallo hello halo"}.
print{"Location of e in hello"}
print{find "e" in "hello"}

def herp
	def derp
		print{"chirp"}
	#derp{}
#herp{}

#yerp yerp
#gorp gorp
#woof woof

print (this condition is true for each foo in [2,4,8]: (foo is divisible by 2))

print ((foo is divisible by 3) for every foo in [3,6,3,9])
print ([3,6,3,9] are divisible by 3)
#smorking 1
#printing "a test of this macro"
print(split "hello" using "e")
print{"g".join{"Hello".split{"l"}}}
x=1; y=2

if (x == 1) :
	print x

str1 = "**derp**"
startAndEnd = "**"

print{"Does "+str1+" start and end with "+startAndEnd+"? " + str{str1 starts and ends with startAndEnd}}

print{"<<foo>>" starts with "<<" and ends with ">>"}

#print{the functions in [isAParameter] that return True for the inputs in [1,2,3,"<<foo>>"]}

import time
function doop(woop, hoop)
	pass
function herp(derp, chirp)
	print{derp + " herp " + chirp}
#print{derp{derp{"Hello"}}}
x = 1
print{"x is " + (x converted to type str)}
print{the type of x}
print{"1" and "2" have the same length}
if (x == 3) :
	print{x}
while (x == 3)
	print{x}
	x += 1
	x *= 1
	x -= 1

class woop:
	pass

for each i in (each integer from 0 to 4)
	print{replace every "l" in "hello" with "r"}
	print{i}
print{replace each "l" with "r" in "hello world"}
print{substring of "hello" from 1 to 5}
print{10 is divisible by 5}
print{10 is divisible by 4}
print{the dimensions of [1, 1, 2, 2]}
print{split the string "Hello world!" using the separator "l"}
print{every occurrence of the string ("l") in the string ("hello")}
print{every integer between (-1) and (3)}
print{all occurrences of "l" in the string "hello"}
print{"The number of times that ('l') occurs in the string ('hello'): " + ((number of times that "l" occurs in the string "hello") converted to type str)}
print{number of times the string 'l' appears in the string "hello world"}
print{convert [1, 2, 3, 4] to str type}
print{"hello"}
print{10 percent of 100}
print{[3, 4, [1, [2, "hello"], 3, [[4, "hello"], "hello"]], 6]}
print{recursively search for 'hello' in the array [1, [2, "hello"], 3, [[4, "hello"], "hello"]]}
print{all occurrences of 1 in the list [1,2,1,4,3,1]}
print{the last index in the array ["Hello", "World!"]}
print{the last index of the array ["Hello", "World!"]}
ensure that (4 != 5)
print{3 < 4 < 5}
print{10 > 7 > 5}
x = 1
if (x == 1) :
	print x
z := 3
print (using the delimiter "e" split the string "hello")

print (with the separator "e" split the string "hello")

theTestArray = [1,5,7,3,2,1]

print{every foo in [3,4,5] that meets the condition (foo > 3)}

print{every number in [1, 2, 3] that is less than 3}

print{every number in [1,2,3,4,5,6,3,2,3,4,3,2,4,5,6,9,(-1)] that is a factor of 3}

print{each number in [1,4,6,3,2,7,6,3] that is divisible by 7}

print{each string in ["hello", "wow", "herp", "derp"] that matches the regular expression "(h|d)erp"}

print{each string in ["hello", "wow", "derp", "herp"] that contains "e"}

print{1 is an integer}
print{(5/2) is an integer}

print{the first letter of "hello"}
print{the last letter of "hello"}
#print{all strings in ["hello", "hallo", "hollow", "hallow"] which match the regular expression "h(e|a|o)llo(w|)"}
print{every match of the regular expression "w(ow|hoa)" in the list ["hey", "wow", "whoa"]}
print{each regular expression in ["h(e)llo", "h(e|a|u)ll(o|s)"] which matches the string "hello"}
print{the first 3 letters of "hello"}
print{the last 3 letters of "hello"}
print{the longest string in ["hello", "what is this", "hey"]}
print{the shortest string in ["hello", "what is this", "hey"]}
print{every match of the regular expression "(derp|(?:w)ha)" in the string "what is a herp or a derp"}
print{pick random from [1,2,3,4,5]}
print{"halo" is an anagram of "hola"}
print{"racecar" is a palindrome}
print{1 is less than 3}
print{5 is an odd number}
print{2 is an even number}
print{2 is a positive number}
print{2 is a negative number}
print{"heheheh1212" does not contain "e"}
print{the type of "foo" is str}
#print{"heheheh1212" is an alphanumeric string}
print{7 is more than 3 but less than 10}
print{7 is less than 10 but more than 3}
#print{3 is no more than 3}
#print{3 is no greater than 3}
#print{3 is no less than 3}
print 3
print("hello" begins with "h")
print(the final 2 letters of "foo")
print (every item in [5,3,6,7,3,12,4,2] that is greater than 4)

function kookoo (q)
	foo = 1
	keep doing this while (foo < 3):
		foo++
		print foo

kookoo{9}
print{the longest string in ["foo", "wppwpp"]}
print{it is true that (10 is a multiple of 5)}
print{it is false that (10 is a multiple of 5)}
#print{10 is not equal to 5}
print{3 ^ 3}
transform the string "Hello stuff" into a file named "exampleOfSomeStuff.txt"
save the string "Hello stuff! Woohoo!" to a file named "exampleOfSomeStuff_1.txt"
print{create a string from the file called "README.md"}
save a copy of the file "exampleOfSomeStuff.txt" called "theSampleCopy.txt"
print{(a list of punctuation marks) arranged randomly}

#print{a random number between 3 and 4}

print{range of integers between 3 and 100}

for current in (split "herp,derp,lol" with the separator ",")
	def randomlyPickedPunctuationMark
		return (pick random from (the list of punctuation marks))
	print{current+(randomlyPickedPunctuationMark{}) + (randomlyPickedPunctuationMark{}) + (randomlyPickedPunctuationMark{})}
print{(7 is 1 more than 6) and (5 is 2 less than 7)}
print{2 to the power of 5}
print{the negation of True}

set goofy to "This is a new macro"
print goofy

print{10 ^ 3}
'''
)

def printUnimplementedMacros(theString):
	theStrings = theString.split("\n");
	theStrings = [name for name in theStrings if name.strip()]
	for current in theStrings:
		try:
			outputString = testMacro(englishToPython.englishToPython, current)
			print("The output of " + current + " is " + outputString)
			print("The result of this output string is ")
			exec outputString
		except Exception as e:
			print e

printUnimplementedMacros('''
whether 10 is greater than 5
factors of 10
the prime factors of 10
greatest common factor of 14 and 12
least common multiple of 12 and 14
5 is a prime number
save the string "This is a file!" to a file named "exampleFile.txt"
write the string "This is a file!" as a file named "exampleFile.txt"
create a string from the file called "exampleFile.txt"
let x be 8
let y be 8
print{"The sum of x and y:"}
print{the square root of (the sum of x and y)}
print{a copy of [1,2,3,4,5]}
print{copy of [1,2,3,4,5]}
print{the type of every variable in [1,"string","hello"]}
print{every variable in [1,"string","hello"] has the same type}
print{delete index 3 in [1,2,3,4]}
print{10 cubed}
print{10 to the power of 3}
print{10 ^ 3}
''')
		
sampleGrammar = [
[["now I say <<foo>>"], "print(<<foo>>)", "final"]
]

#exec testMacro(sampleGrammar, 'now I say "derp"')

print(random.shuffle(["3", "5", "10"]))

#print(q)
