Class(className = "Main", body = [
	includeExternalFile("external"),
	Def(functionName = "mergeStringArray", isStatic=True, returnType = "String", parameterNames = ["stringArray", "separator"], parameterTypes = ["String[]", "string"], body=[
		makevar(arrayDimensions=0, variableType="string", initialValue="\"\"", variableName = "toReturn")+";",
		foreach(typeInArray="string", array="stringArray", variableName="current", body=[
			Set(valueToChange="toReturn", valueToGet=("toReturn"+"+"+"current")),
		]),
		Return("toReturn"),
	]),
	languageSpecific("Java", [
		"import java.util.Arrays;"
	]),
	languageSpecific("JavaScript", [
		'''
		function createArray(length){
			var arr = new Array(length || 0),
			i = length;
			if (arguments.length > 1) {
				var args = Array.prototype.slice.call(arguments, 1);
				while(i--) arr[length-1 - i] = createArray.apply(this, args);
			}
			return arr;
		}
		'''
	]),
	languageSpecific("Python", [
		'''
		import re;
		'''
	]),
	languageSpecific("Ruby", [
		'''
		def RegexMatchesString(string, regex)
			regex = /#{regex}/
			if(string =~ regex) == nil
				return false
			else
				return true
			end
		end
		'''
	]),
	main(body=[
		puts(toString(objectToConvert = args(), convertFrom = "string")),
	]),
	func(functionName = "junk", returnType = "void", parameterNames=[], parameterTypes=[], body=[
		index(theType="string", theObject = "stringName", indexList=[1]),
		index(theType="string[]", theObject = "stringArray", indexList=[1]),
		matchesRegex("theString", "theRegex"),
		contains(containerType="string", checkFor="blah", inObject="theString"),
		Type("varName"),
		size(variable="theArr", theType="int[][]"),
		size(variable="theString", theType="string"),
		arguments(),
		split(string="lol", separator="sep"),
		callFunction(function="startWhile", parameters=["\"Java\"", "\"Java\""]),
		makeVariable(arrayDimensions = [2,2], initialValue = None, variableType = "int", variableName = "theInt"),
		makeVariable(arrayDimensions=[2,2], initialValue=[[1,2],[3,4]], variableType = "int", variableName = "theString"),
		createVariable(initialValue=concatenateStrings(['''"hi! "''', '''"ho!"''', '''"Hee!"''']), arrayDimensions=0, variableName = "newString", variableType="String"),
		initializerList([2,3,4]),
		getArrayIndex(arrayName = "theArr", indexList = [2,2]),
		equals(thing1='''"Hi!"''', thing2='''"Hi!"''', theType="string"),
		defineVariable(variableName = "i", variableType = "int", arrayDimensions=None, initialValue=1),
		Return(toReturn = "1"),
		instanceOf(theValue="lolz", theType="int"),
		Str(objectToConvert="lol", convertFrom = "String"),
		puts(toPrint='''"Hi!"'''),
	]),
	func(functionName="printStringArray", returnType="void", parameterTypes=["String[]"], parameterNames=["theArray"], body = [
		foreach(variableName = "current", typeInArray="string", array="theArray", body=[
			puts("current"),
		]),
	]),
	func(functionName="startWhile", returnType="string", parameterNames=["condition", "lang"], parameterTypes=["string", "string"], body=[
		makeVariable(variableName="theArray", variableType="string", arrayDimensions=[3], initialValue=["\"array\"","\"array2\"","\"array1\""]),
		If(condition=arrayContains(valueToCheck="lang", array="theArray"), body=[
			Return("condition")
		]),
		Else(body=[
			Return("\"Nope!\""),
		])
	]),
	func(functionName="toStringExample", parameterNames=["theInt"], parameterTypes=["int"], returnType="void", body=[
		puts(toPrint=toString(convertFrom="int", objectToConvert="theInt")),
		convert(objectToConvert="theInt", convertFrom="int", convertTo = "str")
	]),
	
	func(functionName="unlessExample", returnType="void", parameterNames=[], parameterTypes=[], body=[
		unless(condition="x == true", body=[
			
		]),
		until(condition = "x == true", body=[
		
		]),
	]),
	
	func(functionName="forEachExample", parameterNames=[], parameterTypes=[], description="Example for for loop", returnType="void", body=[
		enhancedForLoop(variableName = "loopVar", array = "arrName", typeInArray = "int", body=[
			puts(toPrint=accessArray(arrayName="arrName", indexList=["loopVar"]))
		])
	]),

	function(description="Get the length of an integer array", functionName = "intArrayLength", parameterNames=["arr"], parameterTypes=["int[]"], returnType = "int", isDefined=False, requiresTheFunctions=False, body = [
		static(variableName = "theConstant", variableType="int", arrayDimensions=None, initialValue="1"),
		setVar(valueToGet="var1", valueToChange="var2")
	]),
	
	function(functionName = "compare1DIntArrays", description="Return true if the two arrays are identical, and otherwise return false.", parameterNames = ["arr1", "arr2"], parameterTypes = ["int[]", "int[]"], returnType = "boolean", requiresTheFunctions = False, isDefined = False, body=[
		
	]),
	
	proc(parameterNames= ["theString", "theRegex"], parameterTypes = ["string", "string"], requiresTheFunctions=False, returnType = "boolean", isDefined=False, functionName="stringMatchesRegex", description = "Return true if the string matches the regex, and return false otherwise", body =[
		includeForLang(langToInclude = "JavaScript", body=[
			"var theRegExp = new RegExp(\"a|b\", \"i\");"
		])
	]),
	
	method(functionName="getTextFromFile", description = "Return the text of the file from the specified file path.", parameterNames=["filePath"], parameterTypes = ["String"], returnType= "String", isDefined=False, requiresTheFunctions=False, body=[
		includeForLang(langToInclude="Java", body=[
			"//Herp derp. This is Java-Specific code."
		]),
	]),
	
	method(functionName="rangesOverlap", description = "Return true if (x1, y1) overlaps with (x2, y2)", requiresTheFunctions=False, isDefined=False, returnType = "Boolean", parameterNames=["x1", "y1", "x2", "y2"], parameterTypes=["int", "int", "int", "int"], body=[
	
	]),
	
	function(requiresTheFunctions=False, isDefined=False, returnType = "String", functionName = "getComment", description = "Return the comment in the specified language.", parameterNames = ["lang", "comment"], parameterTypes = ["string", "string"], body = [
		If(condition = "lang == \"Java\"", body = [
			
		]),
		If(condition = "lang == \"Python\"", body = [
			
		]),
		If(condition = "lang == \"Ruby\"", body = [
			
		]),
	]),
	function(description = "Example function", requiresTheFunctions=False, isDefined=False, functionName="exampleFunction", returnType = "int", parameterNames = ["parm1", "parm2"], parameterTypes = ["int", "int"], body = [
		comment(comment="First statement in function"),
		comment(comment="Second statement in function"),
		For(initializer = "i=0", condition = "i < 10", increment = "i++", body = [
			comment(comment="Hi!")
		]),
		While(condition= "i < 10", body = [
			comment(comment="Hi!")
		]),
		If(condition = "x == 1", body =[
			comment(comment="Do something here!"),
			If(condition = "x == 1", body =[
				comment(comment="Do something here!")
			]),
			Else(body = [
				comment(comment="Else statement")
			])
		]),
		Else(body = [
			comment(comment="Else statement")
		])
	])
])
