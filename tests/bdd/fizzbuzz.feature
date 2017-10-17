Scenario: FizzBuzz test table
    Given fizz buzz table
    When we have <num> input
    Then it will have <result> output

    Examples:
    | num | result |
    |  1   |  1  |
    |  2   |  2  |
    |  4   |  4  |
    |  3   |  Fizz  |
    |  5   |  Buzz  |
    |  6   |  Fizz  |
    |  8   |  8  |
    |  10   |  Buzz  |
    |  15   |  FizzBuzz  |
    |  30   |  FizzBuzz  |
