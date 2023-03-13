#!/usr/bin/node
// searches the second biggest in the list of integers
const arg = process.argv.slice(2);
if (arg.length <= 1) {
  console.log(0);
} else {
  function compare (a, b) {
    return a - b;
  }
  arg.sort(compare);
  const secBig = arg.length - 2;
  console.log(arg[secBig]);
}
