from typing import List

class OrdinalList(List):
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
    def __getitem__(self, ordinal: str):
        
        number = self._convert_ordinal(ordinal)

        return super().__getitem__(number)

    def __setitem__(self, ordinal: str, value):
        
        number = self._convert_ordinal(ordinal)

        return super().__setitem__(number, value)

    @staticmethod
    def _convert_ordinal(ordinal: str) -> int:

        if not isinstance(ordinal, str):
            raise ValueError("Argument 'ordinal' must be a string, e.g. '1st', '23rd' or '235th'!")

        if len(ordinal) < 3:
            raise ValueError("Argument 'ordinal' is too short to determine ordinal type")

        number = ordinal[:-2]
        last_digit = number[-1]
        suffix = ordinal[-2:].lower()

        try:
            number = int(number)
        except ValueError:
            raise ValueError(f"`{number}` must be an integer!")
        
        if suffix not in ("st", "nd", "rd", "th"):
            raise ValueError("Ordinal number must end with 'st', 'nd', 'rd' or 'th'")
        
        correct_suffix = (
            (last_digit == '1' and suffix == 'st') 
            or (last_digit == '2' and suffix == 'nd') 
            or (last_digit == '3' and suffix == 'rd') 
            or (last_digit in ['0', '4', '5', '6', '7', '8', '9'] and suffix == 'th')
        )
        if not correct_suffix:
            raise ValueError("Suffix does not match the number. '1' must be followed by 'st', '2' must be followed by 'nd', etc.")
        
        if number == 0:
            raise ValueError("You cannot take the 0th element of a sequence, dumbass.")
        if number < 0:
            return number

        return number-1
