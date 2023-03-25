def fizzbuzz(arg):
    if (arg % 5 == 0) and (arg % 3 == 0):
        return 'fizzbuzz'
    if arg % 3 == 0:
        return 'fizz'
    if arg % 5 == 0:
        return 'buzz'
    return str(arg)    #pass nebo 3 tecky - tozn ted se to passne ale pak tam neco dodelam

import pytest

@pytest.mark.parametrize('number', [1, 2, 4, 7])
def test_fizzbuzz_number_returns_number(number):
    assert fizzbuzz(number) == str(number)

@pytest.mark.parametrize('number', [3, 33, 9, 99])
def test_fizzbuzz_number_returns_fizz(number):
    assert fizzbuzz(number) == 'fizz'

@pytest.mark.parametrize('number', [5, 55, 2600])
def test_fizzbuzz_number_returns_buzz(number):
    assert fizzbuzz(number) == 'buzz'

@pytest.mark.parametrize('number', [15, 150, 0])
def test_fizzbuzz_number_returns_fizzbuzz(number):
    assert fizzbuzz(number) == 'fizzbuzz'

def test_fizzbuzz_3_returns_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_exists():
    fizzbuzz

def test_fizzbuzz_can_be_called_w_arg():
    fizzbuzz(0)

def test_fizzbuzz_ret_sth ():
    assert fizzbuzz(0) is not None

def test_fizzbuzz_ret_string():
    assert isinstance(fizzbuzz(0), str)

def test_fizzbuzz_0_returns_fizzbuzz():
    assert fizzbuzz(0) == 'fizzbuzz'

def test_fizzbuzz_1_returns_1():
    assert fizzbuzz(1) == '1'

def test_fizzbuzz_2_returns_2():
    assert fizzbuzz(2) == '2'