module([
	Class("HelloWorld", [
	
		#function returnType functionName parameterNames parameterTypes body
		
		function(parameterNames=["$parm1", "$parm2"], parameterTypes=["Int", "Int"], isStatic=True, returnType="int", functionName="addTwoNumbers", body=[
			Return(add(["$parm1", "$parm2"])),
		]),
		
		function(parameterNames=["a1", "a2", "b1", "b2"], parameterTypes=["Int", "Int", "int", "int"], isStatic=True, returnType="boolean", functionName="rangesOverlap", body=[
			comment("Based on http://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap"),
			conditionalBlock([
				If(condition = And([lessThanOrEqual("a1", "b2"), greaterThanOrEqual("a2", "b1")]), body=[
					Return("True")
				]),
				Else([
					Return("False")
				]),
			]),
		]),
		
		Main([
			seriesOfStatements([
				initializeVar(variableName = "$stringToPrint", variableType = "String", arrayDimensions = None, initialValue = concatenateStrings(["\"Hello \"", "\"World!\""])),
				puts('$stringToPrint'),
				initializeVar(variableName="$theVar", variableType="int", initialValue = 1, arrayDimensions=None),
				puts("$theVar"),
				puts(toString(convertFrom= "int", objectToConvert = getFunctionCall(function = "addTwoNumbers", fromClass = None, parameters = ["1", "2"]))),
				puts(toString(convertFrom= "int", objectToConvert = getFunctionCall(function = "addTwoNumbers", fromClass = None, parameters = ["2", "1"]))),
				puts(getFunctionCall(function = "addTwoNumbers", fromClass = None, parameters = ["3", "1"]))
			]),
		]),
	])
])
