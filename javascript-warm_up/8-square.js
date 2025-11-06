#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(size));
  }
}
