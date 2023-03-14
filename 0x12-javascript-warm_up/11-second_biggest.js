#!/usr/bin/node
// searches the second biggest in the list of integers
const arg = process.argv.slice(2);

function compare (a, b) {
  return a - b;
}
if (arg.length <= 1) {
  console.log(0);
} else {
  arg.sort(compare);
  const secBig = arg.length - 2;
  console.log(arg[secBig]);
}
