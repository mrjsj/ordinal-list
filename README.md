# Ordinal List

Ordinal List is a Python library that extends the functionality of Python's built-in list to use ordinal numbers for indexing. This allows users to access list elements using ordinal notations like '1st', '2nd', '3rd', etc., instead of zero-based indexing.

## Features

- Easy to use interface similar to Python's native list.
- Supports negative indexing similar to Python lists.
- Raises clear and descriptive errors for invalid inputs.

## Installation

To install the Ordinal List library, run the following command in your terminal:

```bash
pip install ordinal-list
```

This will download and install the latest version of Ordinal List from the Python Package Index (PyPI). After installation, you can import and use the library in your Python projects.

## Examples

Here's how to get started with the Ordinal List library:

```python
>> from ordinal_list import OrdinalList
```

Create an OrdinalList with some fruits
```python
>> ordinal_list = OrdinalList(['apple', 'banana', 'cherry'])
```
Access elements using ordinal indices

```python
>> print(ordinal_list['1st'])
apple
>> print(ordinal_list['2nd'])
banana
>> print(ordinal_list['3rd'])
cherry
>> print(ordinal_list['-1st'])
cherry
```

Negative ordinals are also supported, as shown in the example above.

If you try to access an element with an invalid ordinal, the library will raise a descriptive error:
```python
>> try:
>>    print(ordinal_list['0th']) # Invalid ordinal, will raise an error
>> except Exception as e:
>>    print(e)
```


You can also set items using ordinal indices:

```python
>> ordinal_list['1st'] = 'strawberry'
>> print(ordinal_list['1st'])
strawberry
```

And you can extend the list with more items:

```python
>> ordinal_list.extend(['kiwi', 'mango'])
>> print(ordinal_list['5th'])
mango
```
