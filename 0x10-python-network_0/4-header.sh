#!/bin/bash
# Send a GET request to the URL, include the header variable
curl -sH "X-School-User-Id: 98" "$1"
