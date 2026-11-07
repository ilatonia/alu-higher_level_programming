# python-classes

This directory contains Python exercises about classes and objects, built around a `Square` class that grows in features from task to task.

## Requirements

- Python 3, interpreted on Ubuntu 20.04 LTS
- No module imports are allowed
- Code follows the `pycodestyle` (PEP 8) style
- All files are executable and start with `#!/usr/bin/python3`
- Every module and class has a docstring

## Files

| File | Description |
| --- | --- |
| `0-square.py` | An empty class `Square` that defines a square |
| `1-square.py` | `Square` with a private instance attribute `size` set at instantiation (no validation) |
| `2-square.py` | `Square` with optional `size` and type/value validation (`TypeError`, `ValueError`) |
| `3-square.py` | Adds the public instance method `area()` that returns the square's area |
| `4-square.py` | Adds a `size` property getter and setter that validate the value |
| `5-square.py` | Adds `my_print()` that prints the square with the character `#` |
| `6-square.py` | Adds a private `position` attribute with getter/setter, used by `my_print()` to offset the square |

## Example

```python
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(3, (1, 1))
my_square.my_print()
```

Output:

```

 ###
 ###
 ###
```
