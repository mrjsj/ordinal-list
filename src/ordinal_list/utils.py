from typing import List


def convert_ordinal_to_number(ordinal: str, shift: bool = True) -> int:

    if not isinstance(ordinal, str):
        raise ValueError("Argument 'ordinal' must be a string, e.g. '1st', '23rd' or '235th'!")

    if len(ordinal) < 3:
        raise ValueError("Argument 'ordinal' is too short to determine ordinal type")

    number = ordinal[:-2]
    last_digit = number[-1]
    last_two_digits = number[-2:] if len(number) > 1 else ""
    suffix = ordinal[-2:].lower()

    try:
        number = int(number)
    except ValueError:
        raise ValueError(f"`{number}` must be an integer!")
    
    if suffix not in {"st", "nd", "rd", "th"}:
        raise ValueError("Ordinal number must end with 'st', 'nd', 'rd' or 'th'")
    
    correct_suffix = (
        (last_two_digits in {"11", "12", "13"} and suffix == "th")
        or (last_digit == '1' and suffix == 'st' and last_two_digits != "11")
        or (last_digit == '2' and suffix == 'nd' and last_two_digits != "12")
        or (last_digit == '3' and suffix == 'rd' and last_two_digits != "13")
        or (last_digit in {'0', '4', '5', '6', '7', '8', '9'} and suffix == 'th')
    )
    if not correct_suffix:
        raise ValueError("Suffix does not match the number. '1' must be followed by 'st', '2' must be followed by 'nd', etc.")
    
    if number == 0:
        raise ValueError("You cannot take the 0th element of a sequence, dumbass.")

    return number if number < 0 else number - shift


def convert_number_to_ordinal(number: int) -> str:

    if not isinstance(number, int):
        raise ValueError("Argument 'number' must be an integer!")
    
    if number == 0:
        raise ValueError("You cannot take the 0th element of a sequence, dumbass.")
    
    last_digit = abs(number) % 10
    last_two_digits = abs(number) % 100
    
    suffix = ""
    if last_two_digits in {11, 12, 13}:
        suffix = "th"
    elif last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"

    return f"{number}{suffix}"


def ordinal_range(ordinal_start: str, ordinal_end: str) -> List:

    start_number = convert_ordinal_to_number(ordinal_start, shift=False)
    end_number = convert_ordinal_to_number(ordinal_end, shift=False)

    if ordinal_start == ordinal_end:
        return [ordinal_start] 

    reverse = start_number > end_number 
    number = start_number if start_number < end_number else end_number
    last_number = end_number if end_number > start_number else start_number
    ordinal_range = []

    while number <= last_number:
        if number == 0:
            number += 1            
            continue
        
        ordinal_number = convert_number_to_ordinal(number)
        ordinal_range.append(ordinal_number)
        number += 1

    if reverse:
        ordinal_range.reverse()

    return ordinal_range