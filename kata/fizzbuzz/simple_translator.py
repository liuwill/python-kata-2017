def translator(origin):
    if origin % 3 == 0:
        return "Fizz"
    elif origin % 5 == 0:
        return "Buzz"

    return str(origin)
