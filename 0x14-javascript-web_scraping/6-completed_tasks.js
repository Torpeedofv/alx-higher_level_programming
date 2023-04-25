#!/usr/bin/node
const arg = process.argv[2];
const request = require('request');
request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const urlBody = JSON.parse(body);
    // console.log(urlBody)
    const counts = {};
    for (let i = 0; i < urlBody.length; i++) {
    // console.log(urlBody[i]);
      if (urlBody[i].completed === true) {
        const userId = urlBody[i].userId;
        if (!counts[userId]) {
          counts[userId] = 1;
        } else {
          counts[userId]++;
        }
      }
    }
    console.log(counts);
  }
});
