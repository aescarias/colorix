# colorix
Colorix (which stands for 'Color Exchange') is a Python3 module designed for working with colors; specifically color conversion, utilities, and more.

## Installation
The easiest way to install `colorix` is through PIP.
`pip install colorix` or `pip3 install colorix`

**Before installing**, ensure your Python version is 3.6 or above.

## Usage
Currently, `colorix` supports 3 color spaces; RGB, CMYK, and HEX.

The following example demonstrates the standard use of `colorix`.
**NOTE: Results produced by colorix are not guaranteed to be accurate**.

```py
from colorix import RGB # Import the RGB class
rgb = (12, 34, 56) # Set our values
my_result = RGB(*rgb).toCMYK().raw # Get our values
print(my_result) # Print them
>>> (79, 39, 0, 78)

cmyk = my_result # Set our values
my_result = CMYK(*cmyk).toRGB().raw # Get our values
print(my_result) # Print them
>> (12, 34, 56)
```
