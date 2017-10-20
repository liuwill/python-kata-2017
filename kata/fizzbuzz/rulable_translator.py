from abc import ABCMeta, abstractmethod

class Rulable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, result, origin):
        pass

class FizzRuler(Rulable):
    def handle(self, result, origin):
        return handleFizz(result, origin)

class BuzzRuler(Rulable):
    def handle(self, result, origin):
        return handleBuzz(result, origin)

class OtherRuler(Rulable):
    def handle(self, result, origin):
        return handleOther(result, origin)

def translatorRunner(origin, rules):
    result = ""
    for translateRule in rules:
        result = translateRule.handle(result, origin)
    return result

def translator(origin):
    rules = []
    rules.append(FizzRuler())
    rules.append(BuzzRuler())
    rules.append(OtherRuler())

    result = translatorRunner(origin, rules)
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
