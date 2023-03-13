#!/usr/bin/node
const { argv } = require('node:process');

// print a message depending on the number of arguments passed
if (argv.length < 3) {
  console.log('No Argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
