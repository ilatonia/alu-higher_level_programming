# python-test_driven_development

This directory contains Python functions written with test-driven development: each function comes with documented interactive tests (doctest) or unit tests (unittest).

## Requirements

- Python 3, interpreted on Ubuntu 20.04 LTS
- No module imports are allowed in the functions
- Code follows the `pycodestyle` (PEP 8) style
- All files are executable and start with `#!/usr/bin/python3`
- Every module and function has a docstring
- Doctest files are run with `python3 -m doctest -v ./tests/<file>.txt`
- The unittest file is run with `python3 -m unittest tests.6-max_integer_test`

## Files

| File | Description |
| --- | --- |
| `0-add_integer.py` | `add_integer(a, b=98)` adds two integers or floats (floats are casted to integers first) |
| `tests/0-add_integer.txt` | Doctests for `add_integer` |
| `2-matrix_divided.py` | `matrix_divided(matrix, div)` divides all elements of a matrix and rounds them to 2 decimal places |
| `tests/2-matrix_divided.txt` | Doctests for `matrix_divided` |
| `3-say_my_name.py` | `say_my_name(first_name, last_name="")` prints `My name is <first name> <last name>` |
| `tests/3-say_my_name.txt` | Doctests for `say_my_name` |
| `4-print_square.py` | `print_square(size)` prints a square with the character `#` |
| `tests/4-print_square.txt` | Doctests for `print_square` |
| `5-text_indentation.py` | `text_indentation(text)` prints a text with 2 new lines after each `.`, `?` and `:` |
| `tests/5-text_indentation.txt` | Doctests for `text_indentation` |
| `6-max_integer.py` | `max_integer(list=[])` returns the max integer of a list (function provided with the task) |
| `tests/6-max_integer_test.py` | Unit tests for `max_integer` |

## Example

```
$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
...
Test passed.
$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
```
