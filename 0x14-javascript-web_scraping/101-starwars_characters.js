#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[0];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const urlBody = JSON.parse(body).characters;
    const promises = [];
    for (const i of urlBody) {
      promises.push(new Promise(function (resolve, reject) {
        request(i, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      })
      );
    }
    Promise.all(promises).then((names) => {
      for (const i of names) { console.log(i); }
    });
  }
});
