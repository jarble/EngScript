#Test this stuff using polyglotCodeGenerator.py instead of testing it here.
#This version is obsolete! Use polishnotation.py instead.

import cProfile
from crossLanguageParser import printMacroOutputs
import re

#cProfile.run('printMacroOutputs(["(function switchExample (\'x\' ,) ((print 1) ;))"])')

printMacroOutputs([
	#"(while 3)"
#"(create macro '(derp something)' with output 'print(something)' and regular expression '\(derp ([^\s]+)\)')",
#"(derp 'Woohoo!')",
#'''(test the eval function)''',
'''exec("print('woohoo!')")''',
'''((print 1) if (x > 3) unless (x == 10))''',
'''
module
	class 'ASampleClass'
		(
		function switchExample ('x' ,)
			(
			(print '"Hi!"')
			;
			)
		,
		function switchExample2 ('x' ,)
			(
			(print '"Hi!"')
			;
			)
		,
		function switchExample3 ('x' ,)
			(
			(print '"Hi!"')
			;
			)
		)
''',
	'''
module
	function switchExample ('x' ,)
		(
		(
		(print "Hi!") ;
		) ,
		)
	''',
	'''module
	for (int i = 0) (i < 10) (i++)
		(
		((print i) ;)
		) ,''',
	'''('x' *= 3)''',
	'''('x'++)''',
	'''(3 cubed)''',
	'''(7 mod 3)''',
	'''(3 squared)''',
	'''(3 isn't identical to 4)''',
	'''(3 isn't identical to 4)''',
	'''(3 isn't identical to 4)''',
	'''(3 != 4)''',
	'''(3 doesn't equal 4)''',
	'''(! x)''',
	"(oo in food is between f and d)",
	"(oo is between f and d in food)",
	"(3 in base 2 instead of base 10)",
	"(change 3 into base 2 from base 10)",
	"(convert 3 to base 2 from base 10)",
	"(3 converted to base 2 from base 10)",
	"(3 converted from base 10 to base 2)",
	'''
	if x then
		y
	''',
	'''
	while (i > 0)
		while (i > 5)
			print
				'"world"'
	''',

	'''(convert foo from bar into baz)''',
	'''(convert foo into bar from baz)''',
	'''(convert foo from baz into bar)''',
	'''
	while (x > 1)
		cond (
			if (x == 5)
				(
				(print 4) ;
				(print 4) ;
				(print 5)
				)
			,
			elif (x == 7)
				(print 5)
			,
			else
				(print '"Hi!"')
		)
	''',
	'''(int i = 0)''',
	
	'''
	public static void printMessage ([ i ]) ([ int ])
		for (int 'i' = 0) ('i' < 10) ('i' = ('i' + 1))
			(
			(print 'i') ;
			(print ('i' + 1)) ;
			(print ('i' * 2))
			)
	''',
	
	'''((print 3) ; (print 4) ; (print 5))''',
	'''(function named aFunction that returns void with the parameter names ('derp' , 'derp1' , 'derp2') and types ('int' , 'int' , 'int')
		(
			(print '\"Hi!\"') ;
			(print 1)
		)
	)
	''',
	'''public static String aFunction ('derp' , 'derp1' , 'derp2') ('int' , 'int' , 'int')
		(
		(print '\"Hi!\"') ;
		(print 1)
		)
	''',
	'''
	function aFunction ('derp' , 'derp1' , 'derp2')
		(
		(print '\"Hi!\"') ;
		(print 1)
		)
	''',
	'''
	main
		boof
	'''
])



'''

"(if (x == 3) (print 'Whoa!') (else if (x == 1) (print 'Hello') (else (print 'Nope.'))))",

"(foo = bar [ 3 ])",
"(while 3)",
"(if 3)",
"(multiply{((foo , bar) , (biff , boff))})",
"(theArr[(1 , 2 , 3)])",
"(type foo = bar)",
"(int [(2 , 2)] foo = ((1 , 2) , (3 , 4)))",
"(int foo [(2 , 2)] = ((1 , 2) , (3 , 4)))",
"((print 'Hi!') ; (print 'Hello!') ; (return 3))",
"(1 , 2 , 3 , (length of (1 , 4 , 3 , 2)))",
"(switch x (case 1 (print 'Hello')) (case 2 (print 'Hi!')))",
"(case 3 (print 'Hello!'))",
"((return 3) unless (x == 3))",
"(else if (x == 3) (return 3))",
"(else (return 3))",
"(replace each 'e' in 'hello' with 'b')",
"((print 5) while (x == 3))",
"(while (x == 3) (print 5))",
"(print the type of foofoo)",
"(3 is a prime number)",
"((the type of 1) and (the type of 10) are the same)",
"(8 plus 2)",
"(5 > 4)",
"(4 < 5)",
"(12 is divisible by 2)",
"(12 is a multiple of 2)",
"(5 is between (length of [1,2,3,4]) and 7)",
"(5 is between 4 and 7)",
"((a random number between 1 and 10) is between 4 and 7)",
"(print (random number between 1 and 7))",
"(6 to the power of (random number between 1 and 3))",
"((3 is in [1,2,3,4]) and ([1,2,3,4] contains 4))",
"(sum of each element inside [1,2,3,4])",
"(return 3)",
"(3 plus (3 minus 4 minus 5) plus 5)",
"((print 5) if (x equals 3))",
"(if (x equals 1) (print 2))",
"(class aClass extends [class1,class2,class3])",
"(def doSomething (int thing1 , int thing2 , int thing3))",
"((the dimensions of [1,2,3,4]) equal (the dimensions of [4,9,2,4]))",
"(10 and 10 are equal)",
"(10 and (9 + 1) are identical)",
"(10 and (9 + 1) have the same value)",
"(for every value of x starting at 1 and ending at 10, (print x))",
"(for each x from 1 to 10: (print (x + 1)))",
"(True and True)"
])
'''

'''

One possible way to define equivalent statements:

theEquivalentStatements = [
	{"replace each":"l", "in":"hello", "with":"a"},
	{"(in|inside|within)":"hello", "replace each":"l", "with":"a"},
	{"(in|inside|within)":"hello", "change each":"l", "(to|into)":"a"},
	{"change each":"l", "in":"hello", "(to|into)":"a"}
]

theEquivalentStatements2 = [
	{"set":"x","to","y"},
	{"make":"x","(be|become)","y"}
]

'''

print("3 + 4 + 5 + 6".split(" + "))

print(re.split('( \+ )', '1 + 2 * 3 / 4 + 5'))

'''
print("\n\nTest of printMatches")
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(printMatches("(integrate x with respect to y from 1 to 10)"))
pp.pprint(printMatches('(separate x using "a")'))
pp.pprint(printMatches('(set x to 5)'))
pp.pprint(printMatches('(make y become 10)'))
pp.pprint(printMatches('(integrate x^2 with respect to x from 1 to 2)'))
pp.pprint(printMatches('("tree" contains "e")'))
pp.pprint(printMatches('(replace every "e" in "tree" with "a")'))
pp.pprint(printMatches("(good is not bad)"))
pp.pprint(printMatches("(2*3 is equal to 6)"))
pp.pprint(printMatches("('e' is in 'tree')"))
'''

'''
print("\n\n\n")
print(evaluateMacro("('foo' contains 'o')"))
print(evaluateMacro("('o' is inside 'foo')"))
print(evaluateMacro('(1 is an even number)'))
print(evaluateMacro('(1 isn\'t 0)'))
print(evaluateMacro('("derp" is inside "herpderp")'))
print(evaluateMacro('("derp" contains "e")'))
print(evaluateMacro('("e" is part of "derp")'))
print(evaluateMacro('(10 is divisible by 2)'))
print(evaluateMacro('(substring of "hello" between 2 and 4)'))
print(evaluateMacro('(location of "o" in "hello")'))
print(evaluateMacro('("hello" matches "(hello|hi)")'))
print(evaluateMacro('(character in "hello" at position 1)'))
print(evaluateMacro("(location of 3 in [2,3,1,4,4,3,3])"))
print(evaluateMacro("(4 is between 5 and 7)"))
print(evaluateMacro("(replace the string 'e' in the string 'tree' with the string 'a')"))
print(evaluateMacro("(rotate arr1 by 90 degrees)"))
print(evaluateMacro("(string from 1 to 10 in the string 'HelloWorld')"))
print(evaluateMacro("(string between 1 and 10 in 'HelloWorld')"))
print(evaluateMacro("(choose a random number between 1 and 10)"))
print(evaluateMacro("(find a random number between 3 and 10)"))
print(evaluateMacro("(4 to the power of 5)"))
print(evaluateMacro("(shuffle [1,2,3,4] randomly)"))
print(evaluateMacro("(length of [2,2,2])"))
print(evaluateMacro("(size of [1,2,3,4])"))
print(evaluateMacro("(positions of 'l' in 'HelloWorld')"))
print(evaluateMacro("(random item inside [1,2,3,4])"))
print(evaluateMacro("([2,4,3,1] contains every element in [1,2,3,4])"))
print(evaluateMacro("(indices of 4 in [1,2,3,4])"))
print(evaluateMacro("(sort [1,3,4,2] from largest to smallest)"))
print(evaluateMacro("(sort [1,4,3,2] from smallest to largest)"))
print(evaluateMacro("(sort ['will','this','work','properly'] in alphabetical order)"))
print(evaluateMacro("('hello' spelled in reversed order)"))
print(evaluateMacro("(1 inside [1,2,3,4])"))
print(evaluateMacro("(1 is the same as 2-1)"))
print(evaluateMacro("(1 is the same as 2-1)"))
print(evaluateMacro("(1 is an integer)"))
print(evaluateMacro("(the type of 1)"))
print(evaluateMacro("(all occurrences of 'l' within 'hello')"))
print(evaluateMacro("(convert '50' from base 10 to base 2)"))
print(evaluateMacro("([2,5] overlaps with [3,7])"))
print(evaluateMacro("(dimensions of [[1,4],[2,6]])"))
print(evaluateMacro("('hello' from 0 to 1)"))
print(evaluateMacro("(length of (all occurrences of 'l' within 'hello'))"))
'''
def getTrueStatements(listOfStrings):
	toReturn = []
	for current in listOfStrings:
		if(eval(current) == True):
			toReturn += [current]
	return toReturn
	

def isArithmeticExpression(theArr):
	firstOperator = theArr[1]
	if(not isArithmeticOperator(firstOperator)):
		return False
	for idx, current in enumerate(theArr):
		if (idx + 1) % 2 == 0:
			if(current != firstOperator):
				return False
	return True

'''
def testInputString(inputString):
	global data
	data = OneOrMore(nestedExpr()).parseString(inputString)
	print(data)
	firstThing = data[0][0]
	print(getTrueStatements(['data[0][0] == "case"', 'data[0][0] == "foreach"', 'data[0][0] == "default"', 'data[0][0] == "switch"', 'data[0][0] == "if"', 'data[0][0] == "while"', 'data[0][0] == "elif"', 'data[0][0] == "else"', 'data[0][0] == "array"', '(data[0][0] == "method" or data[0][0] == "function" or data[0][0] == "def")', 'isArithmeticExpression(data[0])']))

testInputString('(3 + (4 * 5 * 6) + 5 + 3)')
testInputString('(elif (x == 3))')
testInputString('(while (x == 3))')
testInputString('(switch x)')
testInputString('(case 3)')
testInputString('(default (return 5))')
testInputString('(foreach (return 5))')
'''
