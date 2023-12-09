# 0x0C. Python - Almost a Circle

## Description

This project is part of the ALX Higher Level Programming curriculum. It involves creating a base class (`Base`) and several subclasses to represent geometric shapes, with a focus on testing and documentation.

## Files

1. [tests](./tests) - This directory contains test cases for the classes and methods implemented.
2. [models](./models) - This directory contains the implementation of the classes and methods.

### Base Class

- [base.py](./models/base.py) - Python class `Base` that serves as the base class for all other shapes. It includes methods for serialization and deserialization to and from JSON.

### Rectangle Class

- [rectangle.py](./models/rectangle.py) - Python class `Rectangle` that inherits from `Base`. It represents a rectangle and includes methods for calculating its area and displaying it with the `#` character.

### Square Class

- [square.py](./models/square.py) - Python class `Square` that inherits from `Rectangle`. It represents a square and includes methods for calculating its area and displaying it with the `#` character.

## How to Use

Each file corresponds to a specific class and includes methods for various operations. To use these classes, follow these general steps:

1. Import the desired class:

   ```python
   from models.rectangle import Rectangle

