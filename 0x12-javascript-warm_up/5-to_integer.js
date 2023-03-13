#!/usr/bin/node
// converts an argument to an integer
const [argv1] = process.argv.slice(2);

if (isNaN(argv1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(argv1)}`);
}
