# 0x10. Python - Network #0

## Description

Welcome to the 0x10. Python - Network #0 project repository! This project focuses on networking concepts using Python. You'll learn how to work with HTTP requests, interact with web services, and manage network-related tasks programmatically. This project includes exercises that involve fetching data from the web, parsing HTTP responses, and handling various network protocols.

## Learning Objectives

By the end of this project, you should be able to:

- Understand basic networking concepts.
- Use Python to make HTTP requests.
- Parse and handle HTTP responses.
- Work with different HTTP methods like GET and POST.
- Interact with RESTful APIs using Python.

## Project Files

- **0-body_size.sh**: Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
- **1-body.sh**: Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
- **2-delete.sh**: Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
- **3-methods.sh**: Bash script that takes in a URL and displays all HTTP methods the server will accept.
- **4-header.sh**: Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response, including a header variable.
- **5-post_params.sh**: Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.
- **6-peak.py**: Python script that finds the peak in a list of unsorted integers.
- **100-status_code.sh**: Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.
- **101-post_json.sh**: Bash script that sends a JSON POST request to a URL passed as the first argument and displays the body of the response.
- **102-catch_me.sh**: Bash script that makes a request to `0.0.0.0:5000/catch_me` and gets the message "You got me!".

## How to Use

To use any of the provided scripts, follow these steps:

1. Ensure you have Bash and Python installed on your machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script you want to run.
4. Execute the script using bash or python:

   - For Bash scripts:
     ```bash
     bash script_name
     ```
   
   - For Python scripts:
     ```bash
     python3 script_name.py
     ```

Replace `script_name` with the actual name of the script you want to run.

### Examples

Here are some examples of how to use the scripts:

- Get the size of the body of the response:
  ```bash
  bash 0-body_size.sh https://example.com
  ```

- Send a GET request and display the response body:
   ```bash
   bash 1-body.sh https://example.com
   ```

- Send a DELETE request and display the response body:
   ```bash
   bash 2-delete.sh https://example.com/resource
   ```

- Display all HTTP methods the server will accept:
   ```bash
   bash 3-methods.sh https://example.com
   ```

## Author

- [Martin Olutade](https://github.com/silgenius)
