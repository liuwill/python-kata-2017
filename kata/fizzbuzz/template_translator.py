def translator(origin):
    result = ""

    result = handleFizz(result, origin)
    result = handleBuzz(result, origin)

    result = handleOther(result, origin)
    return result

def handleFizz(builder, origin):
    if isFizz(origin):
        builder += 'Fizz'
    return builder

def handleBuzz(builder, origin):
    if isBuzz(origin):
        builder += 'Buzz'
    return builder

def handleOther(builder, origin):
    if len(builder) == 0:
        builder += str(origin)
    return builder

def isFizz(origin):
    return origin % 3 == 0

def isBuzz(origin):
    return origin % 5 == 0
