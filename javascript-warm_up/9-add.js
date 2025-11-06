#!/usr/bin/node
const arg = process.argv[2];
const arg2 = process.argv[3];
const number = parseInt(arg);
const number2 = parseInt(arg2);

function add (a, b) {
  return a + b;
}

if (isNaN(number) || isNaN(number2)) {
  console.log('NaN');
} else {
  console.log(add(number, number2));
}
