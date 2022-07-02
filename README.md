# ItsUtils

ItsUtils is a small utility-package created by ItsNameless.

The package contains some small utilities that i created for some bigger projects and that i wanted to give to the public, so you can create bigger projects too!

## Installing

To install this package, simply use pip:

```
pip install ItsUtils
```

Or install the development version using:

```
pip install git+https://github.com/TheItsProjects/ItsUtils
```

## Contributing

If you want to give me an idea for a new feature or want to create new features yourself, you can visit the GitHub Repository for this project:

https://github.com/TheItsProjects/ItsUtils

## Features

These are the currently available features:

### StringMath

```py
from its_utils.string_math import StringMath

print(StringMath.full('1*10^45*(3+5)'))
```

This utility calculates the result of a stringified mathematical expression and returns the result as an integer.

It uses the Shunting-Yard algorithm and follows the correct order of operation rules.

### DebugPrompt

```py
from its_utils.debug_prompt import Input

inp = Input.input("Type your name: ", 5)
```

This utility can get an input from the user for a given number of seconds. If no input was given after these seconds, it timeouts and returns None.
