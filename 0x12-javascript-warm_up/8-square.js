#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
} else {
  console.log('Missing size');
}
