module([
	Class("Compiler", [
		comment("Does this work?"),
		languageSpecific("Python", [
			"'''This is a test of language-specific code in Python.'''",
		]),
		function(functionName="subString", returnType="String", isStatic=True, parameterNames=["lang", "theString", "start", "end"], parameterTypes = ["String", "String", "String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"JavaScript,Java"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString','".substring("','start','", "', 'end', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Lua"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"string.sub("','theString','", "','start','", "','end','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"[string range "', "theString", '" "', 'start', "' '", 'end', '"]"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString','"["','start','".."','end','"]"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Python,Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString', '"["', 'start', '":"', 'end', '"]"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"substr("', 'theString', '","', 'start', '","', 'end', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"R"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"substr("', 'theString', '","', 'start', '","', 'end', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString', '".substr("', '","', 'start', '","', 'end', '")"'])),
				]),
				
				
				comment("Despite having the same syntax, the substring function works differently in Racket and Emacs Lisp."),
				elseIf(condition=contains(inObject = split(string='"Emacs Lisp"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"(substring "', 'theString', '" "', 'start', '" "', 'end', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"(substring "', 'theString', '" "', 'start', '" "', 'end', '")"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, subString is not yet defined for \"", "lang"])),
		]),
		function(functionName="regexMatchesString", returnType="String", isStatic=True, parameterNames=["lang", "theString", "regex"], parameterTypes = ["String", "String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"re.compile("','regex','").match("','theString','")"'])),
				]),
			]),
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Java,Scala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString','".matches("','regex','")"'])),
				]),
			]),
			conditionalBlock([
				If(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['regex', '".isMatch("', 'theString', '")"'])),
				]),
			]),
			conditionalBlock([
				If(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"regex.test("', 'theString', '")"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, regexMatchesString is not yet defined for \"", "lang"])),
		]),
		function(functionName="startWhile", returnType="String", isStatic=True, parameterNames=["lang", "condition"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"while "', 'condition', '":"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"REBOL"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"while ["', 'condition', '"] ["'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Lua,Ruby,OCaml,F#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"while "', 'condition', '" do"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Fortran"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"do while ("', 'condition', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"WHILE "', 'condition'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"while [ "', 'condition', '" ]; do"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,JavaScript,PHP,C#,Perl,C++,Haxe,R,AWK,Vala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"while("', 'condition', '"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Tcl,bc"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"while{"', 'condition', '"}{"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for "', 'condition', '" {"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Octave"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"while ("', 'condition', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"While "', 'condition'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, startWhile is not yet defined for \"", "lang"])),
		]),
		function(functionName="typeOf", returnType="String", isStatic=True, parameterNames=["lang", "theObject"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"type("', 'theObject', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"typeof("', 'theObject', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"reflect.TypeOf("', 'theObject', '").Name()"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theObject', '".getClass().getName()"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"Type.typeof("', 'theObject', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"class("', 'theObject', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theObject', '".getType()"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Perl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"ref("', 'theObject', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"getType("', 'theObject', '")"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, typeOf is not yet defined for \"", "lang"])),
		]),
		function(functionName="split", returnType="String", isStatic=True, parameterNames=["lang", "string", "separator"], parameterTypes = ["String", "String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"JavaScript,Java,Python,Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['string', '".split("', 'separator', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"strings.Split("', 'string', '", "', 'separator', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"explode("', 'separator', '", "', 'string', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['string','".Split(new string[] {"','separator','"}, StringSplitOptions.None)"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"[split "', "string", '" "', "separator",'"]"'])),
				]),
				
			]),
			Error(concatenateStrings(["\"In Compiler.py, split is not yet defined for \"", "lang"])),
		]),
		function(functionName="include", returnType="String", isStatic=True, parameterNames=["lang", "fileName"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Java,Python,Haxe,Scala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"import "', "fileName", '";"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"import "', "fileName"])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"using "', "fileName", '";"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"require \'"','fileName','"\'"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, include is not yet defined for \"", "lang"])),
		]),
		function(functionName="startForEach", returnType="String", isStatic=True, parameterNames=["lang", "array", "variableName", "typeInArray"], parameterTypes = ["String", "String", "String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for "',"variableName",'" in "',"array",'":"'])),
				]),
				ElseIf(condition=contains(inObject = split(string='"F#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for "',"variableName",'" in "',"array",'" do"'])),
				]),
				
				ElseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"foreach "',"variableName",'" "',"array",'" {"'])),
				]),
				
				ElseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for i in ${"','variableName','"[@]}; do"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Lua"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for _,"','variableName','" in "','array','" do"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C++"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for("', "typeInArray", '" & "', "variableName", '" : "', "array", '"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["array", '".each do |"', "variableName", '"|"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for "','variableName','" := range "','array','"{"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for("',"variableName",'" in "',"array",'"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"foreach ("',"array",'" as "',"variableName",'"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["array",'".forEach(function("',"variableName",'"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#,Vala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"foreach ("',"typeInArray",'" "',"variableName",'" in "',"array",'"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"for("','typeInArray','" "','variableName','" : "','array','"){"'])),
				]),
				ElseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"For Each "',"variableName",'" As "',"typeInArray ",'" In "', 'array'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, startForEach is not yet defined for \"", "lang"])),
		]),
		function(functionName="charAt", returnType="String", isStatic=True, parameterNames=["lang", "theString", "index"], parameterTypes = ["String", "String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python,JavaScript,Ruby,C#,PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["theString", '"["', "index", '"]"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Java,Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString','".charAt("','index','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"[string index "', "string", '" "', "index", '"]"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString','" !! "','index'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"string([]rune("','theString','")["','index','"])"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Lua"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"string.sub("','theString','","','index','" + 1,"','index','" + 1)"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, charAt is not yet defined for \"", "lang"])),
		]),
		function(functionName="arrayContains", returnType="String", isStatic=True, parameterNames=["lang", "valueToCheck", "array"], parameterTypes = ["String", "String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["valueToCheck", '" in "', "array"])),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['array', '".indexOf("', 'valueToCheck', '") !== -1"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['array','".include?("','valueToCheck','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"Lambda.has("', 'array', '", "', 'valueToCheck', '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"in_array("', "array", '", "', 'valueToCheck', '") !== -1"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['array','".Contains("','valueToCheck','")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"Arrays.asList("','array','").contains("','valueToCheck','")"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, arrayContains is not yet defined for \"", "lang"])),
		]),
		function(functionName="setVar", returnType="String", isStatic=True, parameterNames=["lang", "valueToGet", "valueToChange"], parameterTypes = ["String", "String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python,C#,Java,PHP,JavaScript,Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["valueToChange", '" = "', "valueToGet", '";"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, setVar is not yet defined for \"", "lang"])),
		]),
		function(functionName="arrayLength", returnType="String", isStatic=True, parameterNames=["lang", "array"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python,Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"len("', "array", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,JavaScript,Ruby,Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["array", '".length"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["array", '".Length"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Emacs Lisp,Scheme,Racket,Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"(length "', 'array', '")"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, arrayLength is not yet defined for \"", "lang"])),
		]),
		function(functionName="stringLength", returnType="String", isStatic=True, parameterNames=["lang", "theString"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"C#,JavaScript,Python,Go,Ruby,Haxe,Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					comment("Do this when the string length function is the same as the array length function."),
					Return(getFunctionCall(function = "arrayLength", fromClass = "Compiler", parameters=["lang", "theString"])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"[string length "',"theString",'"]"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"cross-language"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"stringLength("',"theString",'")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Lua"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"string.len("','theString','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"AWK"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"length("','theString','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"R"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"nchar("','theString','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"("','string-length ', 'theString','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"strlen("','theString','")"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Java"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['theString','".length()"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"Len("','"theString"', '")"'])),
				]),
				
			]),
			Error(concatenateStrings(["\"In Compiler.py, stringLength is not yet defined for \"", "lang"])),
		]),
		function(functionName="Error", returnType="String", isStatic=True, parameterNames=["lang", "message"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"raise Exception("', "message", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"throw new Exception("','message','");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript,Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"throw "','message','";"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"throw new Exception("','message','");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haskell,Scheme"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"(error "','message', '")"'])),
				]),
			]),
			
			Error(concatenateStrings(["\"In Compiler.py, Error is not yet defined for \"", "lang"])),
		]),
		function(functionName="getComment", returnType="String", isStatic=True, parameterNames=["lang", "comment"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Bash,AWK,Ruby,Perl,R,Tcl,bc,Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"# "', 'comment'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas,Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(["\"'\"", "comment"])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Fortran"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"! "', "comment"])),
				]),
				elseIf(condition=contains(inObject = split(string='"OCaml"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"(*"', "comment", '"*)"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,Vala,C#,JavaScript,Haxe,Scala,Go,C,C++,PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"//"', "comment"])),
				]),
				elseIf(condition=contains(inObject = split(string='"MATLAB,Octave,Erlang,Prolog"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"%"', "comment"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Lua,Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"-- "', "comment"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['";"', "comment"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Emacs Lisp"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"\""', "comment", '"\""'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, getComment is not yet defined for \"", "lang"])),
		]),
		function(functionName="getClassBeginning", returnType="String", isStatic=True, parameterNames=["lang", "className"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"class "', "className", '":"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"Public Class "', "className"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"class "', "className"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"public class "', "className", '"{"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go,Haxe,C++,PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"class "', "className", '"{"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"function "', 'className', '"(){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Perl,Lua,Bash,Racket,Common Lisp,Tcl,bc"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, getClassBeginning is not yet defined for \"", "lang"])),
		]),
		function(functionName="puts", returnType="String", isStatic=True, parameterNames=["lang", "toPrint"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python,Perl,PHP,AWK"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"print("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"bc"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"print "', "toPrint"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Octave"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"printf("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"MATLAB"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"disp("', "toPrint", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"PRINT "', "toPrint"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"(display "', "toPrint", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"putStr("', "toPrint", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"(echo "', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C++"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"cout << "', "toPrint", '";"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"console.log("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,Groovy"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"System.out.println("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"Console.WriteLine("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"Console.WriteLine("', "toPrint", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"System.Console.WriteLine("', "toPrint", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"puts("', "toPrint", '")"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"puts "', "toPrint"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"trace("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"fmt.Println("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Scala,Vala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"println("', "toPrint", '");"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Lua"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"io.write("', "toPrint", '")"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, puts is not yet defined for \"", "lang"])),
		]),
		function(functionName="getFileExtension", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Lua"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"lua"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"vb"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"bc"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"bc"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Vala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"vala"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"AWK"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"AWK"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"R"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"r"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Erlang"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"erl"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Fortran"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"for"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"tcl"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"rkt"'),
				]),
				elseIf(condition=contains(inObject = split(string='"MATLAB"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"m"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"sh"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"hs"'),
				]),
				elseIf(condition=contains(inObject = split(string='"C++"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"cpp"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"py"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Perl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"pl"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Java"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"java"'),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"js"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"hx"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"rb"'),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"cs"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"go"'),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"php"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, getFileExtension is not yet defined for \"", "lang"])),
		]),
		function(functionName="startMain", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Java,Groovy"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"public static void main(String[] args){"'),
				]),
				elseIf(condition=contains(inObject = split(string='"MATLAB"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"function main"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"cross-language"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"main("'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Visual Basic"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"Sub Main()"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"Public Shared Sub Main()"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"PUBLIC SUB Main()"'),
				]),
				elseIf(condition=contains(inObject = split(string='"C++"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"int main( int argc, const char* argv[] ){"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Python,bc,Tcl,JavaScript,Perl,PHP,Lua,Ruby,Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"function main {"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"main = do"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"func main(){"'),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"static int Main(string[] args){"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"static function main() {"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Vala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"void main() {"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, startMain is not yet defined for \"", "lang"])),
		]),
		function(functionName = "endCodeBlock", isStatic=True, returnType="String", parameterNames = ["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"AWK,bc,Tcl,R,Java,Scala,Squirrel,JavaScript,C#,Haxe,Perl,PHP,Go,C++,Vala,Dylan"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"}"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Python,Haskell,F#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
				elseIf(condition=contains(inObject = split(string='"Racket,Common Lisp,Emacs Lisp"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('")"'),
				]),
				elseIf(condition=contains(inObject = split(string='"REBOL"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"]"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Lua,Ruby,MATLAB,Oz"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"end"'),
				]),
				elseIf(condition=contains(inObject = split(string='"cross-language"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"]),"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endCodeBlock is not yet defined for \"", "lang"])),
		]),
		function(functionName="endIf", returnType="String", isStatic=True, parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"bc,Tcl,REBOL,Vala,AWK,R,F#,Python,Java,JavaScript,C#,cross-language,C++,Perl,PHP,Go,Haxe,Haskell,Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ada,Bash,Lua,Ruby,Octave,MATLAB,Gambas,Visual Basic,Visual Basic .NET,Fortran,OCaml"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endIf is not yet defined for \"", "lang"])),
		]),
		function(functionName="startElse", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"else:"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,AWK,JavaScript,Haxe,PHP,C#,Go,Perl,C++,C,Tcl,R,Vala,bc"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"else {"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Ada,Bash,Ruby,Lua,Haskell,MATLAB,Octave,Gambas,OCaml,Fortran,F#,Oz,Nemerle"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"else"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"(else"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"Else"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, startElse is not yet defined for \"", "lang"])),
		]),
		function(functionName="getClassEnding", returnType="String", isStatic=True, parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"PHP,Python,Ruby,Java,C#,cross-language,Go,Groovy,Haxe,JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"C++"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"};"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Perl,Lua,Bash,Haskell,bc"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"End Class"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, getClassEnding is not yet defined for \"", "lang"])),
		]),
		function(functionName="endElse", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Tcl,R,Vala,Python,F#,Java,JavaScript,Haxe,PHP,C#,cross-language,Perl,C++,Go,Haskell,Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ada,Bash,Lua,Ruby,Visual Basic,Visual Basic .NET,Octave,MATLAB,Gambas,Fortran"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endElse is not yet defined for \"", "lang"])),
		]),
		function(functionName="endElseIf", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Tcl,Vala,AWK,R,Python,F#,Java,JavaScript,Haxe,PHP,C#,cross-language,Perl,C++,Go,Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ada,Bash,Lua,Ruby,Haskell,Visual Basic,Visual Basic .NET,MATLAB,Octave,Gambas,Fortran,OCaml"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endElseIf is not yet defined for \"", "lang"])),
		]),
		function(functionName="endWhile", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"bc,Tcl,REBOL,Vala,AWK,R,F#,Python,Java,Haxe,JavaScript,C#,Perl,cross-language,Ruby,C++,Lua,PHP,Go,MATLAB"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash,OCaml"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"done"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Fortran"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"enddo"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Ada"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"end loop;"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Octave"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"endwhile"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"End While"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"WEND"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endWhile is not yet defined for \"", "lang"])),
		]),
		function(functionName="endMethod", isStatic=True, returnType="String", parameterNames=["lang", "methodName"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"bc,Tcl,Vala,REBOL,Common Lisp,Emacs Lisp,AWK,R,C++,F#,PHP,Lua,Python,Java,JavaScript,C#,Haxe,Perl,cross-language,Ruby,Go,Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haskell,OCaml"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
				elseIf(condition=contains(inObject = split(string='"Ada"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"end "', 'methodName', '";"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"End Sub"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"END"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"}"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Octave"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"endfunction"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Fortran"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"end function "', 'methodName'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endMethod is not yet defined for \"", "lang"])),
		]),
		function(functionName="endForEach", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Tcl,F#,C++,Python,Java,C#,Haxe,Go,PHP,Ruby,Lua,Go,Vala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"});"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Ada"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"});"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"Next"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"NEXT"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"done"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endForEach is not yet defined for \"", "lang"])),
		]),
		function(functionName="endFor", isStatic=True, returnType="String", parameterNames=["lang", "increment"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('increment'),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,JavaScript,C#,cross-language,Ruby,Go,C++,Perl,PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endFor is not yet defined for \"", "lang"])),
		]),
		function(functionName="startIf", isStatic=True, returnType="String", parameterNames=["lang", "condition"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if "', "condition", '":"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"If "', "condition"])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"REBOL"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if ["', 'condition', '"] ["'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Octave"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if "', "condition"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"("', "condition"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Java,JavaScript,C#,C,C++,Perl,Haxe,PHP,R,AWK,Vala,bc,Squirrel"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if("', "condition", '"){"'])),
				]),

				
				elseIf(condition=contains(inObject = split(string='"Tcl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if{"', "condition", '"}{"'])),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if "', "condition", '" {"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if [ "', "condition", '" ] then"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Fortran"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if ("', "condition", '") then"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"IF "', "condition", '" THEN"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haskell,OCaml,Lua,Ruby,F#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"if "', "condition", '" then"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, startIf is not yet defined for \"", "lang"])),
		]),
		function(functionName="startElseIf", isStatic=True, returnType="String", parameterNames=["lang", "condition"], parameterTypes = ["String", "String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Java,Vala,JavaScript,C#,C++,Perl,Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"else if("', "condition", '"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"else if "', "condition", '" {"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"OCaml"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"else if "', "condition", '" then"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"ElseIf "', "condition", '" Then"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Racket"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"("', "condition"])),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"elseif("', "condition", '"){"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"MATLAB"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"elseif "', "condition"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"elif "', "condition", '":"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"F#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"elif "', "condition", '" then"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"elsif "', "condition"])),
				]),
				elseIf(condition=contains(inObject = split(string='"Lua"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"elseif "', "condition", '" then"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"elif [ "', "condition", '" ] then"'])),
				]),
				elseIf(condition=contains(inObject = split(string='"Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(concatenateStrings(['"else if "', "condition", '" then"'])),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, startElseIf is not yet defined for \"", "lang"])),
		]),
		function(functionName="args", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"sys.argv"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Java"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"args"'),
				]),
				elseIf(condition=contains(inObject = split(string='"C#"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"Environment.GetCommandLineArgs()"'),
				]),
				elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"process.argv"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"ARGV"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Go"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"os.Args"'),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"$argv"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, args is not yet defined for \"", "lang"])),
		]),
		
		function(functionName="endMain", isStatic=True, returnType="String", parameterNames=["lang"], parameterTypes = ["String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Java,Vala,cross-language,C#,Haxe,Go,Scala,Perl"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return(getFunctionCall(function = "endCodeBlock", fromClass = "Compiler", parameters=["lang"])),
				]),
				elseIf(condition=contains(inObject = split(string='"C++"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"return 0; }"'),
				]),
				elseIf(condition=contains(inObject = split(string='"PHP,JavaScript,Python,Lua,Ruby,Haskell,Racket,Tcl,bc"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('""'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"Bash"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"}\\nmain"'),
				]),
				
				elseIf(condition=contains(inObject = split(string='"MATLAB"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"end"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"End Sub"'),
				]),
				elseIf(condition=contains(inObject = split(string='"Gambas"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
					Return('"END"'),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, endMain is not yet defined for \"", "lang"])),
		]),
		function(functionName="getCorrespondingTypeWithoutBrackets", isStatic=True, returnType="String", parameterNames=["lang", "theType"], parameterTypes=["String","String"], body=[
			conditionalBlock([
				If(condition=contains(inObject = split(string='"Int,int,Integer"', separator='","'), containerType="String[]", checkFor = "theType"), body=[
					conditionalBlock([
						If(condition=contains(inObject = split(string='"Python,Java,C#,C,C++,Vala,cross-language"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"int"'),
						]),
						elseIf(condition=contains(inObject = split(string='"PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"integer"'),
						]),
						elseIf(condition=contains(inObject = split(string='"Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"Integer"'),
						]),
						elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"Int"'),
						]),
						elseIf(condition=contains(inObject = split(string='"JavaScript"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"number"'),
						]),
						elseIf(condition=contains(inObject = split(string='"Haskell"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"Num"'),
						]),
						elseIf(condition=contains(inObject = split(string='"Ruby"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"fixnum"'),
						]),
					]),
				]),
				elseIf(condition=contains(inObject = split(string='"boolean,Boolean,bool"', separator='","'), containerType="String[]", checkFor = "theType"), body=[
					conditionalBlock([
						If(condition=contains(inObject = split(string='"Python,Java,PHP"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"boolean"'),
						]),
					]),
				]),
				elseIf(condition=contains(inObject = split(string='"String,str,string"', separator='","'), containerType="String[]", checkFor = "theType"), body=[
					conditionalBlock([
						If(condition=contains(inObject = split(string='"Python"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"str"'),
						]),
						
						elseIf(condition=contains(inObject = split(string='"C#,JavaScript,Go,PHP,C++"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"string"'),
						]),
		
						elseIf(condition=contains(inObject = split(string='"Java,Haxe,Haskell,Visual Basic,Visual Basic .NET"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"String"'),
						]),
					]),
				]),
				elseIf(condition=contains(inObject = split(string='"Void,void"', separator='","'), containerType="String[]", checkFor = "theType"), body=[
					conditionalBlock([
						If(condition=contains(inObject = split(string='"Python,Java,C#,Vala"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"void"'),
						]),
						elseIf(condition=contains(inObject = split(string='"Haxe"', separator='","'), containerType="String[]", checkFor = "lang"), body=[
							Return('"void"'),
						]),
					]),
				]),
			]),
			Error(concatenateStrings(["\"In Compiler.py, getCorrespondingTypeWithoutBrackets is not yet defined for \"", "lang", '" and the type "', "theType"])),
		]),
	]),
])
