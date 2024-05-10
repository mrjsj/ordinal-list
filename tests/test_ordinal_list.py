import pytest
from ordinal_list import OrdinalList, ordinal_range
from ordinal_list.utils import convert_number_to_ordinal

def test_ordinal_list_get_item():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    assert ordinal_list["1st"] == "apple"
    assert ordinal_list["2nd"] == "banana"
    assert ordinal_list["3rd"] == "cherry"
    assert ordinal_list["-1st"] == "cherry"

    ordinal_list.extend(range(4, 14))
    assert ordinal_list["11th"] == 11
    assert ordinal_list["12th"] == 12
    assert ordinal_list["13th"] == 13
    assert ordinal_list["-1st"] == 13

def test_ordinal_list_set_item():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    ordinal_list["1st"] = "strawberry"
    assert ordinal_list["1st"] == "strawberry"

    ordinal_list["-1st"] = "coconut"
    assert ordinal_list["-1st"] == "coconut"

    ordinal_list.extend(range(4, 14))
    ordinal_list["11th"] = "avocado"
    ordinal_list["12th"] = "durian"
    ordinal_list["13th"] = "passion fruit"
    assert ordinal_list["11th"] == "avocado"
    assert ordinal_list["12th"] == "durian"
    assert ordinal_list["13th"] == "passion fruit"

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
    with pytest.raises(ValueError):
        _ = ordinal_list["11st"]
    with pytest.raises(ValueError):
        _ = ordinal_list["12nd"]
    with pytest.raises(ValueError):
        _ = ordinal_list["13rd"]

def test_ordinal_list_invalid_negative_ordinal():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(IndexError):
        _ = ordinal_list["-4th"]  # Out of range negative ordinal

def test_ordinal_list_nonexistent_positive_ordinal():
    ordinal_list = OrdinalList(["apple", "banana", "cherry"])
    with pytest.raises(IndexError):
        _ = ordinal_list["10th"]  # Out of range positive ordinal

def test_convert_number_to_ordinal_single_digits():
    assert convert_number_to_ordinal(1) == "1st"
    assert convert_number_to_ordinal(2) == "2nd"
    assert convert_number_to_ordinal(3) == "3rd"
    assert convert_number_to_ordinal(4) == "4th"

def test_convert_number_to_ordinal_teens():
    assert convert_number_to_ordinal(11) == "11th"
    assert convert_number_to_ordinal(12) == "12th"
    assert convert_number_to_ordinal(13) == "13th"

def test_convert_number_to_ordinal_other_tens():
    assert convert_number_to_ordinal(21) == "21st"
    assert convert_number_to_ordinal(22) == "22nd"
    assert convert_number_to_ordinal(23) == "23rd"
    assert convert_number_to_ordinal(24) == "24th"

def test_convert_number_to_ordinal_negative_numbers():
    assert convert_number_to_ordinal(-1) == "-1st"
    assert convert_number_to_ordinal(-2) == "-2nd"
    assert convert_number_to_ordinal(-3) == "-3rd"
    assert convert_number_to_ordinal(-4) == "-4th"

def test_convert_number_to_ordinal_invalid_input():
    with pytest.raises(ValueError):
        convert_number_to_ordinal("a")

def test_ordinal_range_simple():
    assert ordinal_range("1st", "3rd") == ["1st", "2nd", "3rd"]

def test_ordinal_range_with_negative_ordinals():
    assert ordinal_range("-3rd", "-1st") == ["-3rd", "-2nd", "-1st"]

def test_ordinal_range_with_mixed_ordinals():
    assert ordinal_range("1st", "-1st") == ["1st", "-1st"]

def test_ordinal_range_same_start_end():
    assert ordinal_range("2nd", "2nd") == ["2nd"]

def test_ordinal_range_invalid_ordinals():
    with pytest.raises(ValueError):
        ordinal_range("0th", "2nd")

def test_ordinal_range_invalid_type():
    with pytest.raises(ValueError):
        ordinal_range(1, 3)        