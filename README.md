EngScript is an intuitive and extensible English-like programming language.

EngScript is a dialect of the English language that can be automatically translated into Python code.
In other words, you can write programs in plain English and automatically compile them to Python code.

It's MIT-licensed, so it can be used in open-source software projects as well as commercial ones.

For a working demo of EngScript, see [main.py](main.py).

The language's grammar is defined in [englishToPython.py](englishToPython.py).

Some useful code samples:
----
	#Print the first 3 letters of a word
	print (the first 3 letters of "Hello")
	
	#Repeat an action a certain number of times.
	repeat 3 times:
		print "Hello!"
	
	#Check whether a number is prime
	x = 15
	
	if ((x is a prime number) or (x is divisible by 5)) :
		print x
	
	#Create a string from a file
	print{create a string from the file called "README.txt"}
	
	#Save a string as a file
	print{save the string "Woohoo!" to a file called "ExampleText.txt"}
	
	#Get the first few letters of a string
	print{the first 3 letters of "EngScript"}
	#This prints "Eng".
