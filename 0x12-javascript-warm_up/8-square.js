#!/usr/bin/node
// a script that prints a square
const arg = process.argv[2];
if (!arg) {
  console.log('Missing size');
} else if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let j = 0; j < arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
