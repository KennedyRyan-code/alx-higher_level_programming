#!/bin/bash
# URL as the first argument to the script
# Send a request to the URL and display the size of the body of the response
url=$1

curl -sI $url | awk '/Content-Length/{print $2}'
