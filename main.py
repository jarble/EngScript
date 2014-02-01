from libraries import syntaxRules

#import syntaxRules from libraries as herpy

import englishToPython
testMacro = syntaxRules.testMacro

exec testMacro(englishToPython.englishToPython,
'''
#This is some EnglishScript code.

from libraries import syntaxRules as herpy
import pythonFunctions

#These are EngScript's built-in Python functions.

import re
import numpy
import choice from random
import time

print{the greatest common factor of 25 and 100}
#print{the common factors of [10, 14, 100, 25]}

print{"Hi!"}.
print{["hello", "world", "herp", "derp"] in alphabetical order}.
print{arrange ["hello", "world", "herp", "derp"] in alphabetical order}
print{["hello", "world", "herp", "derp"] arranged in alphabetical order}
print{the biggest number in [3,4,5,3,2]}
#Each of these macros are defined using makeDefinitionList.
print{the first 2 items in ["foo", "bar", "baz"]}
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

if x == 1
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
if (x == 3)
	print{x}
while (x == 3)
	print{x}
	x += 1
	x *= 1
	x -= 1
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
if (x == 1)
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
print{create a string from the file called "README.txt"}
save a copy of the file "exampleOfSomeStuff.txt" called "theSampleCopy.txt"
'''
)

def printUnimplementedMacros(theString):
	theStrings = theString.split("\n");
	theStrings = [name for name in theStrings if name.strip()]
	for current in theStrings:
		try:
			testMacro(englishToPython.englishToPython, current)
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
''')
		
sampleGrammar = [
[["now I say <<foo>>"], "print(<<foo>>)", "final"]
]

#exec testMacro(sampleGrammar, 'now I say "derp"')
