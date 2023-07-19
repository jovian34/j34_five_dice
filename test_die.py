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
        roll = die_one.roll()
        assert roll in [1, 2, 3, 4, 5, 6]
        assert roll not in [0, 7]

def test_set_size_method_exists_and_takes_param():
    die_one = die.Die()
    try:
        die_one.set_size(10)
        assert True
    except:
        assert False

def test_set_size_method_changes_die_size():
    die_one = die.Die()
    die_one.set_size(10)
    assert die_one.size == 10

def test_non_std_die_rolls_in_range():
    die_one = die.Die()
    die_one.set_size(10)
    rolls = []
    for i in range(50):
        rolls.append(die_one.roll())
    assert 10 in rolls
    assert 11 not in rolls