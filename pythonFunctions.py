def recursiveArraySearch(toFind, theArray):
	print("Calling recursiveArraySearch")
	print("recursively search for "+str(toFind)+" in the array "+str(theArray))
	allIndices = []
	def recursiveArraySearch1(toFind1, theArray1, allIndices, currentIndex):
		#print("Searching within " + str(theArray1))
		
		thingToAdd = [i for i, x in enumerate(theArray1) if x == toFind1]
		#print("To add to the result: " + str(thingToAdd))
		#print("Current index: " + str(currentIndex))
		
		allIndices += [currentIndex + thingToAdd]
		for i in range(0, len(theArray1)):
			if type(theArray1[i]) == list:
				recursiveArraySearch1(toFind1, theArray1[i], allIndices, currentIndex+[i])
	recursiveArraySearch1(toFind, theArray, allIndices, [])
	#print("All indices: " + str(allIndices))
	return allIndices

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def derp(hi):
	return "derp " + hi
def isAParameter(theInput):
	if(type(theInput) == str):
		if theInput.startswith("<<") and theInput.endswith(">>"):
			return True
	return False
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
def functionsMatchingInputs(theFunctions, theInputs, toReturn):
	theOutputDictionary = {}
	for currentFunction in theFunctions:
		theOutputDictionary[currentFunction] = []
		for currentInput in theInputs:
			currentOutput = currentFunction(currentInput)
			if currentOutput == toReturn:
				theOutputDictionary[currentFunction] += [currentInput]
	return theOutputDictionary

def gcd(a,b): 
  if b == 0: 
    return a 
  else: 
    return gcd(b, (a%b)) 

def gcd_list(l):
  result=l[0] 
  for i in range(1, len(l)): 
    result=gcd(result,l[i]) 
  return result
  
def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def is_prime(a):
    return all(a % i for i in xrange(2, a))

print gcd_list([10, 5, 14,])

def writeStringToFile(fileName, theText):
	with open(fileName, "w") as text_file:
		text_file.write(theText)

def stringFromTextFile(fileName):
	with open (fileName, "r") as myfile:
		return myfile.read()
		
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

