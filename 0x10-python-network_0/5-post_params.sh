#!/bin/bash
# Send a POST request to the URL, include the variables
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
