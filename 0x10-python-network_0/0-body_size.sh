#!/bin/bash
# URL as the first argument to the script
url=$1

# Send a request to the URL and display the size of the body of the response
curl -sI $url | grep -i "Content-Length" | awk '{print $2}'
