
## What are the difference in python between a script, a module, a package and.a library?
In Python, scripts, modules, packages, and libraries are all ways to organize and use code, but they serve different purposes and have distinct characteristics. Here's a breakdown of each:
### Script
**Definition**: A script is a Python file intended to be run directly. It typically contains code that performs a specific task or a series of tasks.  
**Purpose**: Scripts are often used for automation, data processing, or any task that needs to be executed as a standalone program.  
**Example**: `data_analysis.py` that processes and analyzes data when executed.
### Module
**Definition**: A module is a single Python file that can be imported and used in other Python code. It can define functions, classes, and variables.  
**Purpose**: Modules help organize code into reusable components.  
**Example**: `math.py` containing mathematical functions that can be imported using `import math`.
### Package
**Definition**: A package is a collection of modules organized in a directory hierarchy. It includes an `__init__.py` file to indicate that the directory is a package (Although from python 3.3 you no longer need to define the __init__.py file).  
**Purpose**: Packages help organize related modules into a single directory structure, making it easier to manage large codebases.  
**Example**: A package named `mypackage` might look like this:
### Library
**Definition**: A library is a collection of modules and packages that provide a set of functionalities. It can be a single module, a package, or a collection of packages.  
**Purpose**: Libraries are designed to be reused across different projects and can include a wide range of functionalities.  
**Example**: The `requests` library is a popular library for making HTTP requests. It includes multiple modules and packages.
### Summary
- **Script**: Standalone Python file intended to be run directly.
- **Module**: Single file of Python code that can be imported.
- **Package**: Directory of modules with an `__init__.py` file.
- **Library**: Collection of modules and packages providing a set of functionalities.


## Ternary Conditional Expression in Python
A ternary conditional expression in Python is a concise way to perform an if-else check within a single line of code. It's also known as a conditional expression or inline if-else.
### Syntax
The syntax for a ternary conditional expression is:
```python
value_if_true if condition else value_if_false
```
### Example
Here's a simple example:
```python
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
```
### Usage in f-strings
You can also use ternary conditional expressions within f-strings:
```python
myHashMap = {1: 'a', 2: 'b', 3: 'c'}
print(f"{'Yes' if 2 in myHashMap else 'No'}")
```

## Lambda Expression in Python

A **lambda expression** in Python is a small anonymous function defined using the `lambda` keyword. Lambda expressions can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere.
### Syntax
The syntax for a lambda expression is:
```python
lambda arguments: expression
```
### Basic Examples
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```
### Using lambda with map
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```
### Using Lambda with filter
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```
### Using Lambda with sorted
```python
points = [(1, 2), (3, 1), (5, -1)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, -1), (3, 1), (1, 2)]
```
#### When to Use Lambda Expressions
- When you need a small function for a short period.
- When you want to pass a simple function as an argument to higher-order functions like map, filter, or sorted.

## Arguments and Parameters in Python
In Python, **arguments** and **parameters** are terms used to describe the values passed to functions and the variables that receive those values.
### Parameters
**Definition**: Parameters are the variables listed inside the parentheses in the function definition.\
**Purpose**: They act as placeholders for the values that will be passed to the function.\
**Example**:
  ```python
  def greet(name):
      print(f"Hello, {name}!")
  ```
### Arguments
**Definition**: Arguments are the actual values passed to the function when it is called.\
**Purpose**: They provide the data that the function will use.\
**Example**:
  ```python
  def greet(name):
      print(f"Hello, {name}!")
  greet("Alice")
  ```
### Types of arguments:
**Positional Arguments**: Passed to the function in the order they are defined.
```python
def add(a, b):
    return a + b

result = add(2, 3)  # 2 and 3 are positional arguments
```
**Keyword Arguments**: Passed to the function by explicitly naming each parameter and assigning a value.
```python
def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Alice", message="Good morning")  # name and message are keyword arguments
  ```
**Default Arguments**: Parameters that have a default value if no argument is provided.
```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # Uses the default message "Hello"
  ```
**Variable-Length Arguments**: Allows a function to accept an arbitrary number of arguments.
- ***args**: For non-keyword variable-length arguments.
```python
def add(*args):
    return sum(args)

result = add(1, 2, 3)  # args is (1, 2, 3)
  ```
- ****kwargs**: For keyword variable-length arguments.
```python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", message="Good morning")  # kwargs is {'name': 'Alice', 'message': 'Good morning'}
  ```