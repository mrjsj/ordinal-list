import pytest
from ordinal_list import OrdinalList

def test_ordinal_list_get_item():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    assert ordinal_list["1st"] == "apple"
    assert ordinal_list["2nd"] == "banana"
    assert ordinal_list["3rd"] == "cherry"
    assert ordinal_list["-1st"] == "cherry"

def test_ordinal_list_set_item():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    ordinal_list["1st"] = "strawberry"
    assert ordinal_list["1st"] == "strawberry"

    ordinal_list["-1st"] = "coconut"
    assert ordinal_list["-1st"] == "coconut"

def test_ordinal_list_invalid_index():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(ValueError):
        _ = ordinal_list["0th"]

def test_ordinal_list_extend():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    ordinal_list.extend(["kiwi", "mango"])
    assert ordinal_list["5th"] == "mango"

def test_ordinal_list_invalid_ordinal_type():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(ValueError):
        _ = ordinal_list[1]  # Not a string

def test_ordinal_list_invalid_ordinal_format_short():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(ValueError):
        _ = ordinal_list["1"]  # Too short, missing suffix

def test_ordinal_list_invalid_ordinal_format_long():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(ValueError):
        _ = ordinal_list["1sth"]  # Incorrect suffix

def test_ordinal_list_invalid_ordinal_number():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(ValueError):
        _ = ordinal_list["0th"]  # Zero is not a valid ordinal

def test_ordinal_list_invalid_suffix_for_number():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(ValueError):
        _ = ordinal_list["2st"]  # Incorrect suffix for the number

def test_ordinal_list_invalid_negative_ordinal():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(IndexError):
        _ = ordinal_list["-4th"]  # Out of range negative ordinal

def test_ordinal_list_nonexistent_positive_ordinal():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(IndexError):
        _ = ordinal_list["10th"]  # Out of range positive ordinal    