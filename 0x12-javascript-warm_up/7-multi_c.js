#!/usr/bin/node
const arg = process.argv[2];

// Convert the argument to an integer
const x = parseInt(arg);

// Check if the argument can be converted to an integer
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
