from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert(jar.size == 0)
    assert(jar.capacity == 12)
    jar = Jar(3, 15)
    assert(jar.size == 3)
    assert(jar.capacity == 15)
    # jar = Jar(-1)

def test_ValueError():
    with pytest.raises(ValueError):
        jar = Jar(0, "12")
    with pytest.raises(ValueError):
        jar = Jar(-1)



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(15)


def test_withdraw():
    jar = Jar(5)
    jar.withdraw(4)
    assert str(jar) == "🍪"

    with pytest.raises(ValueError):
        jar = Jar(2)
        jar.withdraw(4)

