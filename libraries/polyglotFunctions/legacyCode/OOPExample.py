module([
	Class("OOPExample", [
		privateMember(variableName="theInt", variableType="int", initialValue="4", arrayDimensions=None),
		constructor(className="OOPExample", parameterNames=["int1", "int2"], parameterTypes=["int", "int"], body=[
			setVar(valueToChange=this('theInt'), valueToGet='int1'),
		]),
		
		function(isStatic=False, functionName="getTheInt", returnType="int", parameterNames=[], parameterTypes=[], body=[
			Return(this('theInt'))
		]),
	]),
	newObject(className = "OOPExample", objectName = "theObj", parameterList = ['3','3']),
])
