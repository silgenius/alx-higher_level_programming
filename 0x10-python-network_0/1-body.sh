#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -Ls -w "%{http_code}" -o temp_body.txt $1 | grep -q 200 && cat temp_body.txt && rm temp_body.txt
