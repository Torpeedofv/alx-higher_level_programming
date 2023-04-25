#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[0];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const urlBody = JSON.parse(body).characters;
    // console.log(urlBody);
    for (let i = 0; i < urlBody.length; i++) {
      request(urlBody[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
