-- It is possible to create nested conditional statements in Haskell, as demonstrated here. However, every series of conditional statements must end in "else".

-- http://stackoverflow.com/questions/18029940/is-it-possible-to-write-nested-conditional-statements-in-haskell/18030216?noredirect=1#comment26373630_18030216

thing1 x =
    if x > 2 then
        if x < 5 then
            3
        else if x < 10 then
            if x == 6 then
                9
            else
                10
        else
            6
    else
        4

main = do
    putStr(show(thing1 6) ++ "\n")
    putStr(show(thing1 7) ++ "\n")
    putStr(show(thing1 5) ++ "\n")
