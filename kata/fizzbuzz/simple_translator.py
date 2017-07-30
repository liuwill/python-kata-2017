def translator(origin):
    result = str(origin)

    if origin % 3 == 0 and origin % 5 == 0:
        result = "FizzBuzz"
    elif origin % 3 == 0:
        result = "Fizz"
    elif origin % 5 == 0:
        result = "Buzz"

    return result
