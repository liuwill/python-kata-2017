def translator(origin):
    result = ""

    result = handleFizz(result, origin)
    result = handleBuzz(result, origin)

    if result == "":
        result = str(origin)
    return result

def handleFizz(builder, origin):
    if isFizz(origin):
        builder += 'Fizz'
    return builder

def handleBuzz(builder, origin):
    if isBuzz(origin):
        builder += 'Buzz'
    return builder

def isFizz(origin):
    return origin % 3 == 0

def isBuzz(origin):
    return origin % 5 == 0
