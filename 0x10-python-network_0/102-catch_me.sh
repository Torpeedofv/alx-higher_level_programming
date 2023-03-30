#!/bin/bash
#makes a request to a url that causes the server to respond with a message
curl -s -X PUT -d "user_id=98" -H "Origin: You got me!" -L 0.0.0.0:5000/catch_me
