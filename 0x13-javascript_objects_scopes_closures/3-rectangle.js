#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // Create an empty object if w or h is not a positive integer
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print () {
    // Use nested loops to print the rectangle
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
