#!/bin/bash
# Send a request to the URL and display all HTTP methods the server will accept
curl -sI "$1" | grep Allow
