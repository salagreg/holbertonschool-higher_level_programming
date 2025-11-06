#!/usr/bin/node
const arg = process.argv[2];
const number = parseInt(arg);

function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(number));
