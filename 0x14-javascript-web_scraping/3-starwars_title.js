#!/usr/bin/node
const arg = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
