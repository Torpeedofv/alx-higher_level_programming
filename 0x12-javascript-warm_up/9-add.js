#!/usr/bin/node
// print the addition of 2 integers
const [arga, argb] = process.argv.slice(2);
function add (a, b) {
  return a + b;
}
if (process.argv.length === 4) {
  console.log(add(parseInt(arga), parseInt(argb)));
} else {
  console.log(NaN);
}
