def removeParentheses(theString):
	theString1 = theString.replace("(", "")
	theString1 = theString1.replace(")", "")
	theString1 = "(" + theString1 + ")"
	return [[theString1], theString]
