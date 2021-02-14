# __all__
[stackoverflow](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)
> Linked to, but not explicitly mentioned here, is exactly when __all__ is used. It is a list of strings defining what symbols in a module will be exported when from <module> import * is used on the module.

For example, the following code in a foo.py explicitly exports the symbols bar and baz:
```python
__all__ = ['bar', 'baz']

waz = 5
bar = 10
def baz(): return 'baz'
```

These symbols can then be imported like so:

```python 
from foo import *

print(bar)
print(baz)

# The following will trigger an exception, as "waz" is not exported by the module
print(waz)
```
If the __all__ above is commented out, this code will then execute to completion, as the default behaviour of import * is to import all symbols that do not begin with an underscore, from the given namespace.