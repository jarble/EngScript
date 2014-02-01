def cfor(first,test,update):
    while test(first):
        yield first
        first = update(first)
