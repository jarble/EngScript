module([
includeExternalFile("exampleModule"),
Class("languageSpecificStuff", [
languageSpecific("Java", [
		"import java.util.Arrays;"
	]),
	languageSpecific("VBScript", [
		'''
		Sub includeFile(fSpec)
			With CreateObject("Scripting.FileSystemObject")
				executeGlobal .openTextFile(fSpec).readAll()
			End With
		End Sub
		'''
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
	])
])
])
