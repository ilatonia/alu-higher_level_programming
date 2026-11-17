# python-almost_a_circle

This directory contains a small project built around three classes: `Base`, `Rectangle` and `Square`. It covers class inheritance, getters and setters, `*args` and `**kwargs`, JSON serialization, file storage and unit testing.

## Requirements

- Python 3, interpreted on Ubuntu 20.04 LTS
- Code follows the `pycodestyle` (PEP 8) style
- All files are executable and start with `#!/usr/bin/python3`
- Every module, class and method has a docstring
- All classes and methods are unit tested

## Files

| File | Description |
| --- | --- |
| `models/__init__.py` | Makes `models` a Python package |
| `models/base.py` | `Base`: manages the `id` attribute and the JSON representation of instances (`to_json_string`, `from_json_string`, `save_to_file`, `load_from_file`, `create`) |
| `models/rectangle.py` | `Rectangle(Base)`: private `width`, `height`, `x`, `y` with validated getters and setters, `area`, `display`, `__str__`, `update`, `to_dictionary` |
| `models/square.py` | `Square(Rectangle)`: a rectangle with the same width and height, with a `size` getter and setter, `__str__`, `update`, `to_dictionary` |
| `tests/test_models/test_base.py` | Unit tests for `Base` |
| `tests/test_models/test_rectangle.py` | Unit tests for `Rectangle` |
| `tests/test_models/test_square.py` | Unit tests for `Square` |

## Usage

```python
#!/usr/bin/python3
from models.rectangle import Rectangle
from models.square import Square

r = Rectangle(4, 6, 2, 1, 12)
print(r)                       # [Rectangle] (12) 2/1 - 4/6

Square.save_to_file([Square(5), Square(7, 9, 1)])
print(Square.load_from_file()) # a list of Square instances read from Square.json
```

## Tests

Run all the tests from this directory:

```
$ python3 -m unittest discover tests
```
