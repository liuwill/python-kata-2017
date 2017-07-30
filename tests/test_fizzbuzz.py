
from kata.fizzbuzz import simple_translator

def test_origin():
    assert simple_translator.translator(1) == "1"
    assert simple_translator.translator(2) == "2"

def test_fizz():
    assert simple_translator.translator(3) == "Fizz"

def test_Buzz():
    assert simple_translator.translator(5) == "Buzz"

def test_FizzBuzz():
    assert simple_translator.translator(3*5) == "FizzBuzz"
