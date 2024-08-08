# 0x11. Python - Network #1

## Description

Welcome to the 0x11. Python - Network #1 project repository! This project builds upon the networking concepts learned in Python - Network #0. Here, you'll further explore making HTTP requests, handling responses, working with RESTful APIs, and automating web interactions using Python. The exercises in this project will help you deepen your understanding of network programming in Python and enhance your ability to interact with web services programmatically.

## Learning Objectives

By the end of this project, you should be able to:

- Understand advanced networking concepts.
- Use Python's `requests` library to make HTTP requests.
- Handle HTTP responses and errors.
- Work with JSON data and RESTful APIs.
- Automate web interactions using Python scripts.

## Project Files

- **0-hbtn_status.py**: Python script that fetches `https://alx-intranet.hbtn.io/status` and displays the body of the response.
- **1-hbtn_header.py**: Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response.
- **2-post_email.py**: Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.
- **3-error_code.py**: Python script that takes in a URL, sends a request to the URL, and displays the body of the response (handling HTTP errors).
- **4-hbtn_status.py**: Python script that fetches `https://alx-intranet.hbtn.io/status` using the `requests` library and displays the body of the response.
- **5-hbtn_header.py**: Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response using the `requests` library.
- **6-post_email.py**: Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response using the `requests` library.
- **7-error_code.py**: Python script that takes in a URL, sends a request to the URL, and displays the body of the response (handling HTTP errors) using the `requests` library.
- **8-json_api.py**: Python script that takes in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
- **10-my_github.py**: Python script that takes in GitHub credentials (username and personal access token) and uses the GitHub API to display your `id`.

## How to Use

To use any of the provided scripts, follow these steps:

1. Ensure you have Python installed on your machine. If not, install it by following the [Python installation guide](https://www.python.org/downloads/).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script you want to run.
4. Execute the script using python:

   - For Python scripts:
     ```bash
     python3 script_name.py
     ```

Replace `script_name` with the actual name of the script you want to run.

### Examples

Here are some examples of how to use the scripts:

- Fetch the status from a URL:
  ```bash
  python3 0-hbtn_status.py
  ```

- Display the value of the X-Request-Id variable from the header:
   ```bash
   python3 1-hbtn_header.py https://example.com
  ```

- Send a POST request with an email parameter and display the response:
   ```bash
   python3 2-post_email.py https://example.com user@example.com
  ```

- Handle HTTP errors and display the response body:
   ```bash
   python3 3-error_code.py https://example.com
   ```
 

## Author

- [Martin Olutade](https://github.com/silgenius)
   
