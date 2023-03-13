#!/usr/bin/node

const [arg1, arg2] = process.argv.slice(2);

console.log(`${arg1} is ${arg2}`);

/*
const { argv } = require('node:process');

if (argv.length === 2) {
  console.log('undefined is undefined');
}
if (argv.length === 3) {
  console.log(argv[2] + ' is undefined');
}
if (argv.length === 4) {
  console.log(argv[2] + ' is ' + argv[3]);
}
*/
