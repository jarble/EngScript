englishToPython = [
	#Start of final outputs
	[["(get|create|generate) a string from the file (call|nam)ed <<foo>>"], "pythonFunctions.stringFromTextFile(<<foo>>)", "final"],
	[["save the string <<foo>> (as|to) a file (nam|call)ed <<bar>>", "transform the string <<foo>> into a file named <<bar>>", "(create|generate|produce) a file called <<bar>> from a string (call|nam)ed <<foo>>"], "pythonFunctions.writeStringToFile(<<bar>>, <<foo>>)", "final"],
	[["import <<foo>> from <<bar>> as <<baz>>", "from <<bar>> import <<foo>> as <<baz>>", "import <<foo>> as <<baz>> from <<bar>>"], "from <<bar>> import <<foo>> as <<baz>>", "final"],
	[["from <<foo>> import <<bar>>", "import <<bar>> from <<foo>>"], "from <<foo>> import <<bar>>", "final"],
	[["<<foo>> {}"], "<<foo>>()", "final"],
	[["<<foo>> is an anagram of <<bar>>"], "(sorted(<<foo>>) == sorted(<<bar>>))", "final"],
	[["(pick|choose|select|get) random(|ly) (from|in) <<foo>>"], "choice(<<foo>>)", "final"],
	#[["<<type>> <<varName>> (=) <<value>> (;)"], "<<type>> <<varName>> = <<value>>;", "final"],
	[["(|the )(short|small)est string in <<foo>>"], dict(Python="min(<<foo>>, key=len)"), "final"],
	[["(|the )((long|bigg|larg)est) string in <<foo>>"], dict(Python="max(<<foo>>, key=len)"), "final"],
	[["(|the )((bigg|larg|great)est) number in <<foo>>"], dict(Python="max(<<foo>>)"), "final"],
	[["(|the )((small)est) number in <<foo>>"], dict(Python="min(<<foo>>)"), "final"],
	[["(|the )first letter of <<foo>>"], dict(Python="<<foo>>[0]"), "final"],
	[["(|the )last letter of <<foo>>"], "<<foo>>[len(<<foo>>)-1]", "final"],
	
	[["<<foo>> (is an integer)"], "pythonFunctions.representsInt(<<foo>>)", "final"],
	[["(module) <<body>>"], dict(crosslanguage = "module(<<body>>)"), "final"],
	[["(raise) <<foo>>"], "raise <<foo>>", "final"],
	[["(import) <<module>>"], "import <<module>>", "final"],
	[["<<foo>> (converted to type) <<bar>>", "<<foo>> (converted to) <<bar>> (type)"], dict(Python="<<bar>>(<<foo>>)"), "final"],
	[["(the type of) <<foo>>"], dict(Python="type(<<foo>>)"), "final"],
	[["<<foo>> (or) <<bar>>"], dict(Python= "<<foo>> or <<bar>>)", Java= "(<<foo>> || <<bar>>)", JavaScript="(<<foo>> || <<bar>>)"), "final"],
	[["<<foo>> (\< \=) <<bar>>"], dict(Python="(<<foo>> <= <<bar>>)"), "final"],
	[["<<foo>> (\> \=) <<bar>>"], dict(Python="(<<foo>> >= <<bar>>)"), "final"],
	[["((?:(?:t|T)he |)substring of) <<foo>> (from|between) <<bar>> (to|and) <<baz>>", "(substring (?:from)) <<bar>> (to|between) <<baz>> (in) <<foo>>"],
	dict(Python="<<foo>>[<<bar>>:<<baz>>+1]"),
	"final"
	],
	[["((?:the |)length of) <<foo>>"], dict(Python="len(<<foo>>)", crosslanguage="arrayLength(<<foo>>)"), "final"],
	[["<<foo>> (\{) <<bar>> (\})"], dict(Python="<<foo>>(<<bar>>)"), "final"],
	[["((?:for)(?: |)(?:each|every|all)) <<foo>> (in) <<bar>> <<baz>>"], dict(Python="for <<foo>> in <<bar>>:\n#indent\n<<baz>>\n#unindent\n"), "final"],
	[["<<foo>> (rounded up)", "(round) <<foo>> (up)"], dict(Python="math.ceil(<<foo>>)"), "final"],
	[["<<foo>> (rounded down)", "(round) <<foo>> (down)"], dict(Python="math.floor(<<foo>>)"), "final"],
	[["<<foo>> (rounded to the (?:nearest|closest) integer)", "(round) <<foo>> (to the (?:nearest|closest) integer)"], dict(Python="Math.round(<<foo>>)"), "final"],
	[["((?:A |a |)random number (?:between|from)) <<min>> (and|to) <<max>>"], dict(Python="(math.random() * (<<max>> - <<min>>) + <<min>>)"), "final"],
	[["(replace(?: each| every|)(?: occurrence of|)) <<stringToFind>> ((?:in|inside(?: of|)|within)(?:| the string)) <<containingString>> (with) <<replacementString>>"],dict(Python="<<replacementString>>.join(<<containingString>>.split(<<stringToFind>>))"), "final"],
	[["((?:a |A )random number)"], "math.random()", "final"],
	[["<<foo>> (and|&|&&) <<bar>>"], "(<<foo>> and <<bar>>)", "final"],
	[["<<herp>> (\,) <<derp>>"], "<<herp>>, <<derp>>", "final"],
	[["(class) <<name>> <<body>>"], dict(crosslanguage="getClass(<<name>>, [<<body>>])", Python="class <<name>>\n#indent\n<<body>>\n#unindent\n"), "final"],
	[["(default) <<foo>>"], dict(JavaScript="default: { <<foo>> }"), "final"],
	[["(case) <<foo>> <<bar>>"], dict(JavaScript = "case <<foo>>: <<bar>>"), "final"],
	[["(\[) <<foo>> (\])"], {"Python":"[<<foo>>]", "JavaScript":"[<<foo>>]"}, "final"],
	[["(switch) <<condition>> <<statements>>"], dict(JavaScript="switch <<condition>>{ <<statements>> }", crosslanguage="Switch([<<condition>>, <<statements>>]),"), "final"],
	[["(elif|else if|elsif) <<foo>> <<bar>>", "(elif|else if|elsif) <<foo>> (then) <<bar>>"], dict(Python="elif <<foo>>:\n#indent\n<<bar>>\n#unindent\n"), "final"],
	[["((?:E|e)lse) <<foo>>"], "else:\n#indent\n<<foo>>\n#indent\n", "final"],
	[["<<foo>> (\*|times|multiplied by) <<bar>>"], "(<<foo>> * <<bar>>)", "final"],
	[["<<foo>> (>|is (?:more|greater) than) <<bar>>"], "(<<foo>> > <<bar>>)", "final"],
	[["<<foo>> (<|is (?:less) than) <<bar>>"], "(<<foo>> < <<bar>>)", "final"],
	[["<<foo>> (-|minus) <<bar>>", "<<bar>> subtracted from <<foo>>"], "(<<foo>> - <<bar>>)", "final"],	
	[["<<foo>> (is (?:inside|in|within)) <<bar>>", "<<bar>> (contains) <<foo>>", "<<foo>> (is in|in) <<bar>>"], dict(Python="(<<foo>> in <<bar>>)"), "final"],
	[["<<foo>> (plus|\+) <<bar>>", "(the sum of) <<foo>> (and) <<bar>>"], "(<<foo>> + <<bar>>)", "final"],
	[["<<foo>> (divided by|\/) <<bar>>"], "(<<foo>> / <<bar>>)", "final"],
	[["<<foo>> (==|= =|equals|is equal to) <<bar>>"], "(<<foo>> == <<bar>>)", "final"],
	[["<<foo>> (=) <<bar>>"], "<<foo>> = <<bar>>", "final"],
	[["<<foo>> (\^|to the power of|\*\*) <<bar>>"], "(<<foo>> ** <<bar>>)", "final"],
	[["(if) <<foo>> (:) <<bar>>", "(if) <<foo>> (then) <<bar>>", "<<bar>> (if|if and only if) <<foo>>", "(if) <<foo>> <<bar>>"], dict(Python="if <<foo>>:\n#indent\n<<bar>>\n#unindent\n", Java="if(foo){ <<bar>> }", JavaScript="if(foo){ <<bar>> }"), "final"],
	[["((?:|do this |keep doing this )while) <<x>> (\:) <<y>>", "<<y>> (while) <<x>>", "((?:|do this |keep doing this )while) <<x>> <<y>>"], dict(Python="while <<x>>:\n#indent\n<<y>>\n#unindent\n", Java="while(<<x>>){ <<y>> }"), "final"],
	[["(not|\!) <<foo>>"], "(not <<foo>>)", "final"],
	[["<<foo>> (%) <<bar>>"], "(<<foo>> % <<bar>>)", "final"],
	
	[["(function) <<static>> <<returnType>> <<functionName>> <<parameterNames>> <<parameterTypes>> <<body>>"],
	"def <<functionName>> <<parameterNames>>:\n#indent\n<<body>>\n#unindent\n",
	"final"],
	
	[["(for) <<foo>> <<bar>> <<baz>> <<biff>>", "(for) <<foo>> (;) <<bar>> (;) <<baz>> <<biff>>"], dict(JavaScript="for(<<foo>>; <<bar>>; <<baz>>){ <<biff>> }"), "final"],
	
	[["(convert|change) <<foo>> (from base(?:|s)) <<bar>> ((?:to|into)(?:| base)) <<baz>>", 
	"(convert|change) <<foo>> ((?:to|into) base) <<baz>> (from base) <<bar>>",
	"<<foo>> (converted (?:to|into) base) <<baz>> (from base) <<bar>>",
	"<<foo>> (converted from base) <<bar>> ((?:to|into) base) <<baz>>"],
	"convertBases(<<foo>>, <<bar>>, <<baz>>)",
	"final"],
	#["for each foo in bar"]
	[["<<foo>> (\!\=|\! \=) <<bar>>"], {"JavaScript":"(<<foo>> != <<bar>>)", "Python":"(<<foo>> != <<bar>>)"}, "final"],
	[["<<foo>> ((?:recursively divided|divided recursively) into) <<bar>> (by) <<baz>> (arrays)", "(recursively divide) <<foo>> (into) <<bar>> (by) <<baz>> (arrays)", "(divide) <<foo>> (recursively into) <<bar>> (by) <<baz>> (arrays)"], dict(Python="(divide <<foo>> recursively into <<bar>> by <<baz>> arrays)"), "final"],
	[["((?:all matches|(?:each|every) match) of the (?:regex|regular expression)) <<foo>> ((?:in|inside|within) the string) <<bar>>"], dict(Python="re.findall(re.compile(<<foo>>), <<bar>>)"), "final"],
	[["(return) <<toReturn>>"],"return <<toReturn>>", "final"],
	[["<<foo>> (;)"], dict(Python="<<foo>>\n"), "final"],
	[["<<foo>> (;) <<bar>>"], "<<foo>>;\n<<bar>>", "final"],
	[["(def|function) <<functionName>> <<parameterNames>> <<body>>"], dict(Python="def <<functionName>>(<<parameterNames>>):\n#indent\n<<body>>\n#unindent\n", JavaScript="function <<functionName>>(<<parameterNames>>){ <<body>> }"), "final"],
	[["(var) <<foo>> (=) <<bar>>"], dict(JavaScript="var <<foo>> = <<bar>>", Python = "<<foo>> = <<bar>>"), "final"],
	[["<<foo>> (,)"], "<<foo>>, ", "final"],
	[["(def|function|defun) <<functionName>> <<functionBody>>"], dict(Python="def <<functionName>>():\n#indent\n<<functionBody>>\n#unindent\n", JavaScript="function <<functionName>>(){ <<functionBody>> }"), "final"],
	[["(dictionary|associative array) <<foo>> (\=) <<bar>>", "(dictionary|associative array) <<foo>> <<bar>>"], "<<foo>> = { <<bar>> }", "final"],
	[["(list|array) <<foo>> (\=) <<bar>>", "(array) <<foo>> <<bar>>"], "<<foo>> = [ <<bar>> ]", "final"],
	[["(key) <<foo>> ((?:with|and) value) <<bar>>", "(value) <<bar>> ((?:with|and) key) <<foo>>", "<<foo>> (\:|\-\-\>) <<bar>>"], dict(Python = "<<foo>>: <<bar>>"), "final"],
	[["((?:anonymous |)self-(?:evaluating|executing|invoking|calling) (?:anonymous |)function) <<body>>"], dict(JavaScript="{(function(){ <<body>> })()"), "final"],
	[["((?:split|separate)(?:| the string)) <<foo>> ((?:with|using)(?:| the (?:separator|delimiter))) <<bar>>"], dict(Python="<<foo>>.split(<<bar>>)"), "final"],
	[["((?:t|T)he (?:regex|regexp|regular expression)) <<regex>> (matches the string) <<string>>", "((?:t|T)he string) <<string>> (matches the (?:regex|regexp|regular expression)) <<regex>>", "<<string>> (matches the (?:regex|regexp|regular expression)) <<regex>>"], dict(Python="re.compile(<<regex>>).match(<<string>>)"), "final"],
	[["((?:every|each|all) (?:occurrence|appearance|location|index|indice)(?:s|) of(?: the string|)) <<foo>> ((?:in|inside)(?: the string|)) <<bar>>"], dict(Python="[m.start() for m in re.finditer(<<foo>>, <<bar>>)]"), "final"],
	
	[["((?:every|each|all) (?:occurrence|appearance|location|index|indice)(?:s|) of) <<foo>> ((?:in|inside)(?:| the (?:array|list))) <<bar>>"], dict(Python="[i for i, x in enumerate(<<bar>>) if x == <<foo>>]"), "final"],
	[["((?:the |)dimensions of(?: the (?:array|list)|)) <<foo>>"], dict(Python="numpy.array(<<foo>>).shape"), "final"],
	[["(insert|put) <<obj>> (after the index) <<index>> ((?:inside|in) the (?:list|array)) <<list>>"], dict(Python="insertIntoList(<<list>>, <<index>>+1, <<obj>>)"), "final"],
	[["(insert|put) <<obj>> (before the index) <<index>> ((?:inside|in) the (?:list|array)) <<list>>"], dict(Python="insertIntoList(<<list>>, <<index>>, <<obj>>)"), "final"],
	
	[["((?:every|each|all) integer(?:s|) (?:between|from)) <<foo>> (and|to) <<bar>>"], dict(Python="range(<<foo>>+1, <<bar>>)"), "final"],
	[["((?:join|merge) the (?:array|strings)) <<array>> ((?:with|using) the separator) <<separator>>"], dict(Python="<<separator>>.join(<<array>>)"),"final"],
	[["<<foo>> (written|spelled) backwards"], dict(Python="<<foo>>[::-1]"), "final"],
	[["(wait) <<seconds>> (seconds)"], dict(Python="time.sleep(<<seconds>>)"), "final"],
	[["((?:|(?:the|all|each|every) )factor(?:|s) of) <<foo>>"], dict(Python="pythonFunctions.factors(<<foo>>)"), "final"],
	
	[["((?:remove|delete) (?:each|every|all) occurrence(?:s|) of(?: the value|)) <<val>> ((?:from|in) the (?:list|array)) <<the_list>>"], dict(Python="remove_values_from_list(<<the_list>>, <<val>>)"), "final"],
	[["(absolute value of) <<foo>>"], dict(Python="math.fabs(<<foo>>)"), "final"],
	[["(rotate the array) <<foo>> (90 degrees clockwise)"], dict(Python="zip(*<<foo>>[::-1])"), "final"],
	[["(rotate the array) <<foo>> (90 degrees counterclockwise)"], dict(Python="zip(*<<foo>>)[::-1]"), "final"],
	[["((?:understand|define)(?:| the (?:macro|syntax))) <<foo>> (as|as the (?:macro|syntax)) <<bar>>", "((?:define|create|declare|make) (?:a |the |)(?:macro|syntax)(?:| (?:named|called|with the input))) <<foo>> ((?:and|with|(?:that|which) (?:produces|generates|gives)) the (?:output|macro)) <<bar>>"], dict(Python="defMacro(<<foo>>, <<bar>>)\n"), "final"],
	
	[["(the functions in) <<functions>> ((?:that|which) return) <<toReturn>> (for the inputs in) <<inputs>>"], dict(Python="pythonFunctions.functionsMatchingInputs(<<functions>>, <<inputs>>, <<toReturn>>)"), "final"],
	
	[["<<foo>> ((?:start|begin)s with) <<bar>>"], dict(Python="<<foo>>.startswith(<<bar>>)"), "final"],
	[["<<foo>> (ends with) <<bar>>"], dict(Python="<<foo>>.endswith(<<bar>>)"), "final"],
	[["((?:search recursively|recursive(?:|ly) search) for) <<toFind>> (in the array) <<theArray>>", "(search for) <<toFind>> (recursively in the array) <<theArray>>"], dict(Python="pythonFunctions.recursiveArraySearch(<<toFind>>, <<theArray>>)"), "final"],
	[["(every|each) <<item>> (in|inside|within) <<list>> ((?:that|which) (?:satisfie|meet)s the condition) <<conditional>>"], dict(Python="[<<item>> for <<item>> in <<list>> if <<conditional>>]"), "final"],
	[["<<foo>> ((?:|arranged |sorted )in alphabetical order)", "(arrange|sort) <<foo>> (in alphabetical order)"], "sorted(<<foo>>)", "final"],
	
	#End of final outputs, and beginning of non-final outputs
	[["<<foo>> is a prime number"], "pythonFunctions.is_prime{<<foo>>}"],
	[["least common multiple of <<foo>> and <<bar>>"], "pythonFunctions.lcm{<<foo>>, <<bar>>}"],
	[["the greatest common factor of <<foo>> and <<bar>>"], "pythonFunctions.gcd{<<foo>>, <<bar>>}"],
	[["ensure that <<foo>>", "ensure that <<foo>> ;", "<<foo>> (must|should|ought to) be true"], "if (<<foo>> == False) then (raise Exception{'Something is wrong!'})"],
	[["the last index (of|in) the array <<foo>>"], "(the length of <<foo>>) - 1"],
	#[["split the string <<foo>> at index <<bar>>"], "split the string <<foo>> from index <<bar>> to index <<baz>> , "],
	[["<<foo>> ((starts|begins) with) <<bar>> (and ends with) <<baz>>"], "(<<foo>> starts with <<bar>>) and (<<foo>> ends with <<baz>>)"],
	[["<<foo>> ((starts|begins) and ends with) <<bar>>"], "<<foo>> starts with <<bar>> and ends with <<bar>>"],
	
	[["((?:remove|delete) (?:each|every|all) occurrence(?:s|) of(?: the value|)) <<val>> ((?:from|in) the (?:string)) <<the_string>>"], "replace every occurrence of <<val>> in the string <<the_string>> with ''"],
	[["wait <<minutes>> minutes"], "wait (<<minutes>> * 60) seconds"],
	[["wait <<hours>> hours"], "wait (<<hours>> * 60) minutes"],
	[["((?:the )square root of) <<foo>>"], "(<<foo>> to the power of (1 / 2))"],
	[["(function) <<hello>> ((?:always|only) returns) <<hi>>"], "def <<hello>> ((return <<hi>>) ;)"],
	[["<<foo>> ((?:%|percent) of) <<bar>>"], "((<<bar>> / 100) * <<foo>>)"],
	[["<<foo>> (\=) <<bar>> (\+) <<baz>>"], "<<foo>> = (<<bar>> + <<baz>>)"],
	[["<<foo>> (\=) <<bar>> (\-) <<baz>>"], "<<foo>> = (<<bar>> - <<baz>>)"],
	[["<<foo>> (\=) <<bar>> (\^) <<baz>>"], "<<foo>> = (<<bar>> ^ <<baz>>)"],
	[["<<foo>> (\=) <<bar>> (\*) <<baz>>"], "<<foo>> = (<<bar>> * <<baz>>)"],
	[["<<foo>> (\=) <<bar>> (\%) <<baz>>"], "<<foo>> = (<<bar>> % <<baz>>)"],
	[["<<foo>> (is between) <<bar>> (and) <<baz>>"], "(<<bar>> < <<foo>>) and (<<foo>> < <<baz>>)"],
	[["<<foo>> (is greater than or equal to) <<bar>>"], "<<foo>> >= <<bar>>"],
	[["<<foo>> (is less than or equal to) <<bar>>"], "<<foo>> <= <<bar>>"],
	[["<<foo>> (\+ \=) <<bar>>"], "<<foo>> = <<foo>> + <<bar>>)"],
	
	[["<<foo>> (\- =|\-\=) <<bar>>"], "<<foo>> = <<foo>> - <<bar>>"],
	
	[["<<foo>> (\* =) <<bar>>"], "<<foo>> = <<foo>> * <<bar>>"],
	
	[["<<foo>> (\^ =) <<bar>>"], "<<foo>> = <<foo>> ^ <<bar>>"],
	[["<<foo>> (\+ \+|\+\+)"], "<<foo>> += 1"],
	[["<<foo>> (- -|\-\-)"], "<<foo>> -= 1"],
	[["<<foo>> (unless) <<bar>>", "(unless) <<bar>> <<foo>>"], "<<foo>> if (not <<bar>>)"],
	[["<<foo>> (is (?:divisible by|a multiple of)) <<bar>>", "<<bar>> (is a factor of) <<foo>>"], "(<<foo>> % <<bar>>) == 0"],
	[["(until) <<x>> (:) <<y>>", "<<y>> (until) <<x>>"], "<<y>> while (not <<x>>)"],
	[["(for(?: every| each| all|)) <<foo>> (from|between) <<bar>> (to|and) <<baz>> <<biff>>"], "for (var <<foo>> = <<bar>>) (<<foo>> < <<baz>>) (<<foo>> ++) <<biff>>"],
	[["(the product of) <<bar>> (and) <<baz>>"], "<<bar>> multiplied by <<baz>>"],
	[["(the quotient of) <<foo>> (and) <<bar>>"], "<<foo>> divided by <<bar>>"],
	#[["<<foo>> (divided by) <<bar>>"], "<<foo>> / <<bar>>"]
	[["(indices from) <<start>> (to) <<end>> (in|of) <<array>>"], "substring from <<start>> to <<end>> in <<array>>"],
	[["<<array>> (is a) <<numberOfDimensions>> (dimensional array)"], "(the length of (the dimensions of <<array>>)) == <<numberOfDimensions>>"],
	[["(the array) <<array>> (from) <<start>> (to) <<end>>"], "substring of <<array>> from <<start>> to <<end>>"],
	[["<<foo>> (and) <<bar>> (have the same dimensions)"], "(the dimensions of <<foo>>) == (the dimensions of <<bar>>)"],
	[["<<foo>> (and) <<bar>> (have the same length)"], "(the length of <<foo>>) == (the length of <<bar>>)"],
	[["<<foo>> (and) <<bar>> (have the same type)"], "(the type of <<foo>>) == (the type of <<bar>>)"],
	[["<<foo>> ((?:does not|doesn\'t) equal) <<bar>>", "<<foo>> ((?:is not|isn\'t) equal to) <<bar>>"], "(<<foo>> != <<bar>>)"],
	[["<<foo>> (and) <<bar>> (are not equal)"], "<<foo>> does not equal <<bar>>"],
	[["<<foo>> (is (?:identical to|the same as)) <<bar>>", "<<foo>> (and) <<bar>> (are (?:identical|the same))"], "<<foo>> == <<bar>>"],
	[["<<foo>> (does not contain) <<bar>>"], "not (<<foo>> contains <<bar>>)"],
	[["((?:|the )remainder of) <<foo>> (divided by) <<bar>>"], "<<foo>> % <<bar>>"],
	[["(rotate the array) <<foo>> (180 degrees)"], "rotate the array (rotate the array <<foo>> 90 degrees clockwise) 90 degrees clockwise"],
	[["(number of times (?:that|)(?: |)(?:the string|)) <<foo>> ((?:occur|appear)s in(?:| the string)) <<bar>>", "(number of occurrences of(?:| the string)) <<foo>> (in(?:| the string)) <<bar>>"], "length of (all occurrences of <<foo>> in the string <<bar>>)"],
	[["(convert) <<foo>> (to) <<bar>> (type)"], "<<foo>> converted to <<bar>> type"],
	[["(print) <<foo>>"], "print { <<foo>> }"],
	[["(replace each) <<foo>> (with) <<bar>> (in) <<baz>>"], "replace each <<foo>> in <<baz>> with <<bar>>"],
	[["<<foo>> ((?:, |)(?:but|(?:and|but) also|as well as|even though|although|(?:despite|in spite of) the fact that)) <<bar>>"], "<<foo>> and <<bar>>"],
	[["(either) <<foo>> (or) <<bar>>"], "<<foo>> or <<bar>>"],
	[["<<foo>> is (True|true|not (?:F|f)alse)"], "<<foo>> == True"],
	[["<<foo>> is (False|false|(?:not|n\'t) (?:t|T)rue)"], "<<foo>> == False"],
	
	
	[["(if) <<foo>> (\= \=|equals) <<bar>> (then) <<baz>>", "(if) <<foo>> (\= \=|equals) <<bar>> <<baz>>"], "if (<<foo>> == <<bar>>) then <<baz>>"],
	
	[["(if) <<foo>> (\>) <<bar>> (then) <<baz>>", "(if) <<foo>> (\>) <<bar>> <<baz>>"], "if (<<foo>> > <<bar>>) then <<baz>>"],
		
	[["(if) <<foo>> (\<) <<bar>> (then) <<baz>>", "(if) <<foo>> (\<) <<bar>> <<baz>>"], "if (<<foo>> < <<bar>>) then <<baz>>"],
	
	[["(if) <<foo>> (\> \=) <<bar>> (then) <<baz>>", "(if) <<foo>> (\>\=) <<bar>> <<baz>>"], "if (<<foo>> >= <<bar>>) then <<baz>>"],
	
	[["(if) <<foo>> (\< \=) <<bar>> (then) <<baz>>", "(if) <<foo>> (\<\=) <<bar>> <<baz>>"], "if (<<foo>> <= <<bar>>) then <<baz>>"],
	
	[["(if) <<foo>> (\! \=) <<bar>> (then) <<baz>>", "(if) <<foo>> (\!\=) <<bar>> <<baz>>"], "if (<<foo>> != <<bar>>) then <<baz>>"],
	[["<<foo>> (\: \=) <<bar>>"], "<<foo>> = <<bar>>"],
	[["((?:with|using) the (?:delimiter|separator)) <<foo>> ((?:split|separate) the string) <<bar>>"], "split the string <<bar>> using the separator <<foo>>"],
	[["((?:every|each|all) (?:item|number) in) <<array>> ((?:that|which) is greater than) <<number>>"], "every foo in <<array>> that meets the condition (foo > <<number>>)"],
	[["((?:every|each|all) (?:item|number) in) <<array>> ((?:that|which) is less than) <<number>>"], "every foo in <<array>> that meets the condition (foo < <<number>>)"],	
	[["((?:every|each|all) (?:item|number) in) <<array>> ((?:that|which) is (?:divisible by|a multiple of)) <<number>>"], "every foo in <<array>> that meets the condition (foo is a multiple of <<number>>)"],	
	[["((?:every|each|all) (?:item|number) in) <<array>> ((?:that|which) is (?:a factor of)) <<number>>"], "every foo in <<array>> that meets the condition (foo is a factor of <<number>>)"],	
	[["((?:the|all) strings in) <<array>> ((?:that|which) match the (?:regex|regular expression)) <<regex>>", "((?:every|each|all) (?:item|string)(?:s|) in) <<array>> ((?:that|which) (?:match(?:es|) the (?:regex|regular expression))) <<regex>>"], "every foo in <<array>> that meets the condition (foo matches the regex <<regex>>)"],	
	[["((?:every|each|all) (?:item|string|list) in) <<array>> ((?:that|which) (?:contains)) <<regex>>"], "every foo in <<array>> that meets the condition (foo contains <<regex>>)"],
	[["((?:every|each|all) (?:regular expression|regex) in) <<array>> ((?:that|which) (?:match(?:|es) the (?:string))) <<string>>"], "every foo in <<array>> that meets the condition (<<string>> matches the regex foo)"],
	[["((?:every|each|all) match(?:es|) of the (?:regex|regular expression)) <<regex>> (in the (?:list|array)) <<array>>"], "each string in <<array>> which matches the regular expression <<regex>>"],
	[["((?:|the )first) <<foo>> ((?:letter|element|item)s (?:of|in)) <<bar>>"], "substring of <<bar>> from 0 to (<<foo>> - 1)"],
	[["((the |)(last|final)) <<foo>> ((letter|element|item)s (of|in)) <<bar>>"], "substring of <<bar>> from ((length of <<bar>>) - <<foo>>) to (length of <<bar>>)"],
	[["(define the macro) <<herp>> ((?:that|which) means) <<derp>>"], "define the macro <<herp>> with the output <<derp>>"],
	[["<<foo>> is a palindrome"], "(<<foo>> spelled backwards) equals <<foo>>"],
	[["(every) <<foo>> (in) <<bar>> ((?:satisfies|meets) (?:the|this) condition(?:|\:)) <<baz>>"], "<<bar>> == (every <<foo>> in <<bar>> that satisfies the condition <<baz>>)"],
	[["(this condition is true for (?:every|each)) <<foo>> (in) <<bar>> (\:) <<baz>>", "<<baz>> ((?:is true |)for (?:all|each|every)) <<foo>> (in) <<bar>>"], "every <<foo>> in <<bar>> satisfies the condition <<baz>>"],
	[["<<foo>> (are divisible by) <<bar>>"], "(baz is divisible by <<bar>>) for every baz in <<foo>>)"],
	[["def <<foo>>(\{\}) <<bar>>", "def <<foo>> (\{\})(\:) <<bar>>"], "def <<foo>> <<bar>>"],
	[["((?:the |)longest match of the (?:regular expression|regex|regexp)) <<foo>> (in the string) <<bar>>"], "the longest string in (every match of the regular expression <<foo>> in the string <<bar>>)"],
	[["(print) <<foo>> (\.)"], "print <<foo>>"],
	[["<<foo>> ."], "<<foo>>;"],
	[["<<foo>> = <<bar>> ."], "<<foo>> = <<bar>>"],
	[["<<foo>> is an even number"], "(<<foo>> % 2) == 0"],
	[["<<foo>> is an odd number"], "not (<<foo>> is an even number)"],
	[["<<foo>> is a positive number"], "<<foo>> is greater than 0"],
	[["<<foo>> is a negative number"], "<<foo>> is less than 0"],
	[["(split|divide|separate) <<foo>> into <<bar>> equal (parts|pieces)"], "list{pythonFunctions.chunks{<<foo>>, int{len{<<foo>>} / <<bar>>}}}"],
	[["<<bar>> is the type of <<foo>>"], "<<foo>> == (the type of <<bar>>)"],
	[["the type of <<bar>> is <<foo>>"], "(the type of <<bar>>) == <<foo>>"],
	[["<<foo>> (is (greater|more) than) <<bar>> ((and|but) less than) <<baz>>", "<<foo>> (is less than) <<baz>> ((?:and|but) (?:greater|more) than) <<bar>>"], "(<<foo>> < <<baz>>) and (<<foo>> > <<bar>>)"],
	#[["<<foo>> is no(t|) (greater|more) than <<bar>>"], "not (foo > bar)"],
	[["it is true that <<foo>>"], "<<foo>> is true"],
	[["it is (false|(not |un)true) that <<foo>>"], "<<foo>> is not true"],
	[["(the |)greatest common (factor|denominator) of <<foo>>"], "pythonFunctions.gcm{<<foo>>}"],
	[["(save|make|create|generate) a copy of (|the file (|called ))<<foo>> (called|named|and call it|and name it) <<bar>>"], "save the string (create a string from the file called <<foo>>) to a file named <<bar>>"]
	]
