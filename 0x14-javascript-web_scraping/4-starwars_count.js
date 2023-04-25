#!/usr/bin/node
const arg = process.argv[2];
const request = require('request');
request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resultArray = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < resultArray.length; i++) {
      if (resultArray[i].characters) {
        const characters = resultArray[i].characters;

        for (let j = 0; j < characters.length; j++) {
          if (characters[j].includes('18')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  }
});
