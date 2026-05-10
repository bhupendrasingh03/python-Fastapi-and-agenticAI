# python-Fastapi-and-agenticAI
This Repo is all about my python-Fastapi-and-agenticAI

# Python Learning Journey

## Topics Covered

### Functions & Basics
- Creating your first programs in Python
- Functions
- Bugs
- Variables
- Comments
- Strings
- Parameters
- Formatted Strings
    name = "Alice"
    print(f"Hello, {name}!") 
    # Output: Hello, Alice!
- Integers
- Principles of readability
- Floats

---

### Conditionals
- if
- elif
- else
- or
- and
- bool
- match
status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500 | 503: # Using '|' for multiple values
        print("Server Error")
    case _: # Wildcard 'default' case
        print("Unknown Status")

---

### Loops & Collections
- while loops
- for loops
- list
- range
    range(start, stop, step)
    Parameter Type             Description
    start     Optional         The beginning value. Defaults to 0 if omitted. 
    stop      Optional         The sequence stops before this number (it is exclusive).
    step       Optional        The increment (gap) between numbers. Defaults to 1.

    Single Argument: range(5)
    Generates: 0, 1, 2, 3, 4
    
    Two Arguments: range(2, 6)
    Generates: 2, 3, 4, 5
    Starts at 2 and stops just before 6.

    Three Arguments: range(0, 10, 2)
    Generates: 0, 2, 4, 6, 8
    range(0, 10, 2) starts from 0 and increase by 2 each time
    range(10, 0, -2) starts from 10 and decreases by 2 each time


- continue
- break
- len()
- dict
    A built-in data structure used to store data in key-value pairs

---

## Progress
More topics will be added as I continue learning Python 