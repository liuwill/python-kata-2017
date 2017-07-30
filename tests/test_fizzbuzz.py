
from kata.fizzbuzz import simple_translator

def test_origin():
    assert simple_translator.translator(1) == "1"
    assert simple_translator.translator(2) == "2"
