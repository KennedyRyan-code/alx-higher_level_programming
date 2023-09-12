#!/usr/bin/node
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the argument can be converted to an integer
if (!isNaN(size)) {
  if (size > 0) {
    // Loop to print each row
    for (let i = 0; i < size; i++) {
      let row = '';
      // Loop to print X characters for each row
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('');
  }
} else {
  console.log('Missing size');
}
