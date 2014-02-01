module([
	function(returnType="string", parameterTypes=["String", "String"], parameterNames=["$str1", "$str2"], isStatic=True, functionName="sampleFunction", body=[
	
	]),
	
	conditionalBlock([
		If(condition="x==5", body=[
			
		]),
		elseIf("x==1", body=[
			
		]),
		elseStatement(body=[
			
		]),
	]),
	While(condition="x==1", body=[
			
	]),
	
	forEach(array="theArr", variableName="i", typeInArray="String", body=[
	
	]),
	
	For(condition="i < 10", initializer="i = 0", increment="i++", body=[
	
	]),
	
	foreach(typeInArray="string", array="theArr", variableName="currentVar", body=[
	
	]),
	
	Switch("x", [
		case("1", [
		
		])
	]),
	
])
