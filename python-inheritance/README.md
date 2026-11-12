# Python - Inheritance

This project covers inheritance in Python: subclassing built-in types, checking
an object's class with `type`, `isinstance` and `issubclass`, overriding
methods, and calling parent code with `super()`.

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Returns the list of attributes and methods of an object |
| `1-my_list.py` | `MyList`, a `list` subclass with `print_sorted` |
| `2-is_same_class.py` | True if an object is exactly an instance of a class |
| `3-is_kind_of_class.py` | True if an object is an instance of a class or its subclasses |
| `4-inherits_from.py` | True if an object is an instance of a strict subclass |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an unimplemented `area` |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator` |
| `8-rectangle.py` | `Rectangle` with private, validated width and height |
| `9-rectangle.py` | Full `Rectangle` with `area` and `__str__` |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with its own `__str__` |
| `tests/1-my_list.txt` | Doctests for `1-my_list.py` |
| `tests/7-base_geometry.txt` | Doctests for `7-base_geometry.py` |

## Running the tests

```
python3 -m doctest -v ./tests/1-my_list.txt
python3 -m doctest -v ./tests/7-base_geometry.txt
```

## Author

ilatonia
