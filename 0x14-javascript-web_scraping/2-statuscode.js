#!/usr/bin/node
const arg = process.argv[2];
const request = require('request');
request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
