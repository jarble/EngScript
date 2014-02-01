#An online JavaScript program with all function dependencies: http://jsfiddle.net/JPnAF/9/



#print([1,1,1,2,3][0:5])


#This thing is implemented!
def getArrayFromFunctionComment(theComment):
	theComment = theComment[len("requires functions: "):len(theComment)]
	return theComment.split(", ")

#print getArrayFromFunctionComment("requires functions: False")
#print getArrayFromFunctionComment("requires functions: foo, bar, baz, biff, buff")

"function name: getStringFromFileTwo"
"requires functions: getStringFromFile, gorp"
"is defined: False"
"description: Hi this is the description."

"function name: getStringFromFile"
"requires functions: gorp"
"is defined: False"
"description: Hi this izz the description."

"function name: gorp"
"requires functions: False"
"is defined: False"
"description: Hi this izz the description."

"an irrelevant comment"
"another irrelevant comment"

'''This is implemented!'''
def getStringFromFile(fileName):
	with open (fileName, "r") as myfile:
		data=myfile.read();
	return data;

'''This is implemented!'''

def getCommentArrayFromFile(fileName):
	theString = getStringFromFile(fileName)
	
	theStrings = theString.split("\n")
	
	theArr = []
	
	i = 0
	for current in theStrings:
		if(len(current) > 1):
			if(current[0] == '"'):
				if(current[len(current) - 1] == '"'):
					theArr += [current];
					
					#if(current.indexOf('"function name:')):
					
		i = i + 1
	
	for idx, current in enumerate(theArr):
		theArr[idx] = current.strip()
		theArr[idx] = current[1:len(current)-1]
	
	return theArr

def splitTheComment(theComment):
	return theComment.split(": ")

def getTwoDCommentArrayFromFile(theFile):
	theCommentArray = getCommentArrayFromFile(theFile);
	theNewCommentArray = {}
	currentFunctionName = ""
	for current in theCommentArray:
		#print(current)
		theSplitComment = splitTheComment(current)
		#print(theSplitComment)
		if(theSplitComment[0] == "function name"):
			currentFunctionName = theSplitComment[1]
			theNewCommentArray[currentFunctionName] = {}
		elif(theSplitComment[0] == "requires functions"):
			theNewCommentArray[currentFunctionName]["requires functions"] = getArrayFromFunctionComment(current)
		elif(theSplitComment[0] == "is defined"):
			theNewCommentArray[currentFunctionName]["is defined"] = theSplitComment[1]
			#print(theSplitComment)
		elif(theSplitComment[0] == "description"):
			theNewCommentArray[currentFunctionName]["description"] = theSplitComment[1]
			#print(theSplitComment)
	return theNewCommentArray

#print(getCommentArrayFromFile("functionChecker.py"))

#print(getTwoDCommentArrayFromFile("functionChecker.py"))

alreadyCheckedFunctions = []

def printImplementableFunctions(theFile,functionToPrint):
	global alreadyCheckedFunctions;
	theCommentArray = getTwoDCommentArrayFromFile(theFile)
	def requiresFunctions(theFunction):
		return theCommentArray[theFunction]["requires functions"]
	def isDefined(theFunction):
		return theCommentArray[theFunction]["is defined"]
	def theDescription(theFunction):
		return theCommentArray[theFunction]["description"]
	def canBeImplemented(theFunction):
		if(isDefined(theFunction) == "True"):
			return False
		for current in requiresFunctions(theFunction):
			if(current == "False"):
				return True
		for current in requiresFunctions(theFunction):
			if(isDefined(current) == "False"):
				return False
		return True
	def printFunctionInfo(theFunction):
		print(theFunction)
		print("    requires functions: " + str(requiresFunctions(theFunction)))
		print("    is defined: " + isDefined(theFunction))
		print("    description: " + theDescription(theFunction))
		print("    can be implemented: " + str(canBeImplemented(theFunction)))
	for current in requiresFunctions(functionToPrint):
		if current != "False":
			if(isDefined(current) == "False"):
				if(not current in alreadyCheckedFunctions):
					printImplementableFunctions(theFile, current)
	
	if(canBeImplemented(functionToPrint) == True):
		printFunctionInfo(functionToPrint)
	if(not functionToPrint in alreadyCheckedFunctions):
		alreadyCheckedFunctions += [functionToPrint]

#printImplementableFunctions("functionChecker.py", "getStringFromFileTwo")

def functionChecker(thing1, thing2):
	printImplementableFunctions(thing1, thing2);
