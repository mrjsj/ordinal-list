from typing import List, TypeVar
from ordinal_list.utils import convert_number_to_ordinal, convert_ordinal_to_number, ordinal_range

__all__ = (
    "OrdinalList",
    "ordinal_range"
)

_T = TypeVar("_T")


class OrdinalList(List[_T]):
    """
    A custom list class that allows accessing elements using ordinal numbers as strings.

    Inherits from the built-in List class and provides a custom implementation of the
    `__getitem__` method to interpret string ordinals ('1st', '2nd', '3rd', etc.) as indices.

    Parameters
    ----------
    List: The list of elements to initialize the OrdinalList with.

    Examples
    --------
    >>> my_list = OrdinalList(['a', 'b', 'c'])
    >>> my_list['1st']
    'a'
    >>> my_list['2nd']
    'b'
    >>> my_list['3rd']
    'c'

    Negative ordinals are supported, following Python's negative indexing convention.

    Raises
    ------
    ValueError: 
        - If the ordinal is not a string
        - is too short
        - does not end with a correct ordinal suffix
        - does not represent an integer
        - or if the integer part of the ordinal is 0 (since there is no '0th' item).
    """
    def __getitem__(self, ordinal: str) -> _T:
        
        number = convert_ordinal_to_number(ordinal)

        return super().__getitem__(number)

    def __setitem__(self, ordinal: str, value: _T) -> None:
        
        number = convert_ordinal_to_number(ordinal)

        return super().__setitem__(number, value)


