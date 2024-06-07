from fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(11) == 89

def test_fibonacci_1():
    assert fibonacci(8) == 21

def test_fibonacci_2():
    assert fibonacci(14) == 377

def test_fibonacci_3():
    assert fibonacci(17) == 1597

def test_fibonacci_4():
    assert fibonacci(20) == 6765