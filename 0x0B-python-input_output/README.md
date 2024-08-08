# 0x0B. Python - Input/Output

## Description

This project is part of the ALX Higher Level Programming curriculum. It focuses on input and output operations in Python, including file handling, reading and writing to files, and using the `json` format.

## Files

1. [0-read_file.py](./0-read_file.py) - Python function that reads a text file and prints its content.
2. [1-write_file.py](./1-write_file.py) - Python function that writes a string to a text file and returns the number of characters written.
3. [2-append_write.py](./2-append_write.py) - Python function that appends a string at the end of a text file and returns the number of characters added.
4. [3-to_json_string.py](./3-to_json_string.py) - Python function that converts an object to its JSON representation using the `json` module.
5. [4-from_json_string.py](./4-from_json_string.py) - Python function that converts a JSON string to an object using the `json` module.
6. [5-save_to_json_file.py](./5-save_to_json_file.py) - Python function that writes an object to a text file using its JSON representation.
7. [6-load_from_json_file.py](./6-load_from_json_file.py) - Python function that creates an object from a JSON file.
8. [7-add_item.py](./7-add_item.py) - Python script that adds all arguments to a Python list, and then saves them to a file.
9. [8-class_to_json.py](./8-class_to_json.py) - Python function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.
10. [9-student.py](./9-student.py) - Python class `Student` with a method to retrieve a dictionary representation of a `Student` instance.
11. [10-class_to_json.py](./10-class_to_json.py) - Python function that returns the dictionary description with simple data structure for JSON serialization of an object (supports nested classes).
12. [11-student.py](./11-student.py) - Python class `Student` with additional attributes and methods for JSON serialization.
13. [12-pascal_triangle.py](./12-pascal_triangle.py) - Python function that returns a list of lists representing Pascal's triangle of `n` rows.

## AUTHORS

- [Martin Olutade](https://github.com/silgenius)

## How to Use

Each file corresponds to a specific task. Instructions on how to run or use each file are provided within the task's directory.

## Input/Output Usage

File handling in Python involves opening, reading, and writing to files. The `json` module is used for encoding and decoding JSON data.

Example:

```python
# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Using the json module
import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Writing to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading from a JSON file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)

