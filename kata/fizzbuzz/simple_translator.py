def translator(origin):
    result = ""

    if isFizz(origin):
        result = "Fizz"
    if isBuzz(origin):
        result += "Buzz"

    if result == "":
        result = str(origin)
    return result

def isFizz(origin):
    return origin % 3 == 0

def isBuzz(origin):
    return origin % 5 == 0
