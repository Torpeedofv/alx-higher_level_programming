#!/bin/bash
#sends a POST request and display the body of the response
curl -sX POST -d "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" $1
