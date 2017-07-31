
from kata.fizzbuzz import simple_translator
from kata.fizzbuzz import template_translator

def test_origin():
    assert simple_translator.translator(1) == "1"
    assert simple_translator.translator(2) == "2"
    assert simple_translator.translator(4) == "4"

def test_fizz():
    assert simple_translator.translator(3) == "Fizz"

def test_Buzz():
    assert simple_translator.translator(5) == "Buzz"

def test_FizzBuzz():
    assert simple_translator.translator(3*5) == "FizzBuzz"

def test_template_FizzBuzz():
    assert template_translator.translator(30) == "FizzBuzz"

def test_template_fizz():
    assert template_translator.translator(6) == "Fizz"

def test_template_Buzz():
    assert template_translator.translator(10) == "Buzz"

def test_template_origin():
    assert template_translator.translator(8) == "8"
