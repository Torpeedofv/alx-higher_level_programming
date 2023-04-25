#!/usr/bin/node
const arg = process.argv[2];
const fs = require('fs');
// const file = fs.readFileSync(arg, 'utf8');
try {
  const file = fs.readFileSync(arg, 'utf8');
  console.log(file);
} catch (err) {
  console.log(err);
}
