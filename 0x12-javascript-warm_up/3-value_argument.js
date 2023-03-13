#!/usr/bin/node
const { argv } = require('node:process');

// print the first argument passed
argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  if (index === 1) {
    console.log('No argument');
  }
});
