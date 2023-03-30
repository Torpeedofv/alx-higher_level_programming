#!/bin/bash
#sends a JSON Post resquest passed to a URL passed as the first argument
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
