# python-more_classes

This directory contains exercises on Python classes and objects: private
attributes, properties, class attributes, static and class methods, and special
methods such as `__str__`, `__repr__` and `__del__`.

All files are written for Python 3, follow the PEP 8 style (pycodestyle) and
are documented (module, class and methods). No module is imported.

## Files

| File | Description |
| --- | --- |
| `0-rectangle.py` | Empty `Rectangle` class |
| `1-rectangle.py` | `Rectangle` with private, validated `width` and `height` properties |
| `2-rectangle.py` | Adds `area()` and `perimeter()` |
| `3-rectangle.py` | Adds `__str__` to print the rectangle with `#` |
| `4-rectangle.py` | Adds `__repr__` so `eval(repr(r))` recreates the rectangle |
| `5-rectangle.py` | Adds `__del__` that prints `Bye rectangle...` |
| `6-rectangle.py` | Adds the `number_of_instances` class attribute |
| `7-rectangle.py` | Adds the `print_symbol` class attribute |
| `8-rectangle.py` | Adds the static method `bigger_or_equal(rect_1, rect_2)` |
| `9-rectangle.py` | Adds the class method `square(size=0)` |
