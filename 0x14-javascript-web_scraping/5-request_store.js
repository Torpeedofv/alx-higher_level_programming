#!/usr/bin/node
const arg = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
request(arg[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFileSync(arg[1], body);
  }
});
