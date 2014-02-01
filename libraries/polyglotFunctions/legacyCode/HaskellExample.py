module([
	comment("This is a Haskell code example."),
	function(returnType="Int", functionName = "$product1", parameterNames=["$x", "$y"], isStatic=True, parameterTypes=["Int", "Int"],  body=[
		If(greaterThan("$x", "$y"), [
			Return("$x")
		]),
		elseIf(lessThan("$x", "$y"), [
			Return("$y")
		]),
		Else([
			Return(add(["$x", "$y"]))
		])
	]),
	function(returnType="void", functionName = "$hello", parameterNames = ["$answer"], parameterTypes = ["String"], isStatic=True, body = [
		Switch("$answer", [
			case('"yes"', [
				puts('"Hooray!"')
			]),
			case('"no"', [
				puts('"Oh no!"')
			]),
			default([
				puts('"Say what?"'),
			]),
		]),
	]),
	main([
		statement(initializeVar(variableName="$theArr", variableType = "Int", arrayDimensions=[3,2], initialValue=[[1,2],[1,2],[1,2]])),
		puts(toString(objectToConvert = index(theObject="$theArr", indexList=[1,1], theType = "int"), convertFrom = "int")),
		puts(toString(objectToConvert=callFunction(fromClass=None, function="$product1", parameters=["3", "3"]), convertFrom="int")),		
		statement(callFunction(fromClass=None, function="$hello", parameters=['"yes"']))
	]),
])
