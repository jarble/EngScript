module([
	Class("HelloWorld", [
		function(parameterNames=["$parm1", "$parm2"], parameterTypes=["Int", "Int"], isStatic=True, returnType="int", functionName="addTwoNumbers", body=[
			Return(add(["$parm1", "$parm2"])),
		]),
		
		function(parameterNames=["$parm1", "$parm2"], parameterTypes=["Int", "Int"], isStatic=True, returnType="void", functionName="sampleFunction", body=[
			switch("$parm1", [
				case("1", [
					puts('''"It's 1!"''')
				]),
				case("2", [
					puts('''"It's 2!"''')
				]),
				default([
					puts('''"It's something else!"''')
				]),
			]),
		]),
		
		function(parameterNames=["$parm1"], parameterTypes=["Int"], isStatic=True, returnType="String", functionName="sampleFunction1", body=[
			Return(concatenateStrings(['"Derp"', "$parm1"])),
		]),
		
		Main([
			seriesOfStatements([
				puts("\"Hello World!\""),
				initializeVar(variableName="$theVar", variableType="String", initialValue = '"Hello!!!"', arrayDimensions=None),
				puts("$theVar"),
				getFunctionCall(function = "sampleFunction", fromClass = None, parameters = ["1", "2"]),
				getFunctionCall(function = "sampleFunction", fromClass = None, parameters = ["2", "1"]),
				getFunctionCall(function = "sampleFunction", fromClass = None, parameters = ["3", "1"]),
				puts(getFunctionCall(function = "sampleFunction1", fromClass = None, parameters = ['"Hi"']))
			]),
		]),
	])
])
