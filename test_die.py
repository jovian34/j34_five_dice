import pytest
import die


def test_instance_of_die_class_exists():
    die_one = die.Die()
    assert die_one

def test_get_standard_size_of_die():
    die_one = die.Die()
    assert die_one.size == 6

def test_roll_method_exists():
    die_one = die.Die()
    try:
        die_one.roll()
        assert True
    except:
        assert False

def test_std_die_rolls_in_range():
    die_one = die.Die()
    for i in range(10):
        die_one.roll()
        assert die_one.roll() in [1, 2, 3, 4, 5, 6]

def test_set_size_method_exists():
    die_one = die.Die()
    try:
        die_one.set_size()
        assert True
    except:
        assert False