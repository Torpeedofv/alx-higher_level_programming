#!/usr/bin/node
// computes and prints a factorial
function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return (a) * factorial(a - 1);
  }
}
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
