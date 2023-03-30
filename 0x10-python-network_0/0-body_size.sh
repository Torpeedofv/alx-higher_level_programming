#!/bin/bash
# displays the size of the body of the response from a url
curl -s w $1 | wc -c
