from pytest_bdd import given, when, then, scenario
from kata.fizzbuzz import simple_translator
from kata.fizzbuzz import template_translator

@scenario(
    'fizzbuzz.feature',
    'FizzBuzz test table',
    example_converters=dict(num=int, result=str)
)
def test_outlined():
    pass


@given('fizz buzz table')
def start_cucumbers():
    print 'Start FizzBuzz'


@when('we have <num> input')
def have_input(num):
    assert isinstance(num, int)


@then('it will have <result> output')
def should_have_left_cucumbers(num, result):
    assert isinstance(result, str)
    assert template_translator.translator(num) == result
    assert simple_translator.translator(num) == result
