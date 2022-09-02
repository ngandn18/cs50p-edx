from seasons import minutes
import pytest

def test_minutes():
    # assert(minutes("2008-11-21") == "Seven million, two hundred forty thousand, three hundred twenty")
    # assert(minutes("2018-11-21") == "One million, nine hundred eighty-one thousand, four hundred forty")
    assert(minutes("2021-08-27") == "Five hundred twenty-seven thousand forty minutes")
    assert(minutes("2022-03-27") == "Two hundred twenty-one thousand, seven hundred sixty minutes")
    assert(minutes("2020-08-20") == "One million, sixty-two thousand, seven hundred twenty minutes")


    with pytest.raises(SystemExit):
        assert(minutes("Jan 11 2020")) == "Invalid date"
    with pytest.raises(SystemExit):
        assert(minutes("01-11-2020")) == "Invalid date"
    with pytest.raises(SystemExit):
        assert(minutes("Jan-11-2020")) == "Invalid date"


