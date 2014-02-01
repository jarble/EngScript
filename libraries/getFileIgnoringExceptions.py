from polyglotCodeGenerator import *

os.chdir("polyglotFunctions")
def getFileInLanguage(current, fileNames = None):
	global lang
	
	if(fileNames == None):
		fileNames = glob.glob("*.py")
		for n,i in enumerate(fileNames):
			fileNames[n] = fileNames[n][:-3]
	
	for fileName in fileNames:
		try:
			lang = current;
			with open (fileName + ".py", "r") as myfile:
				data=myfile.read()
			theFile = eval(data);
			
			theFile = removeWhitespace(theFile);
			
			theDir = "generatedFunctions/"+lang+"Functions/"
			if not os.path.exists(theDir):
				os.makedirs(theDir)
			text_file = open(theDir + fileName + "."+getFileExtension(), "w")
			text_file.write(theFile)
			text_file.close()
		except Exception as e:
			thingToAdd = traceback.format_exc()
			print(thingToAdd)

def getFileIgnoringExceptions(theLangs, fileNames=None):
	if(type(theLangs) == str):
		theLangs = [theLangs]
	for current in theLangs:
		getFileInLanguage(current, fileNames)
