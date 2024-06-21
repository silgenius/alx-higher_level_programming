#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the Rectangle constructor with size for both width and height
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X'; // Default to 'X' if c is undefined
    }

    for (let i = 0; i < this.height; i++) {
      let block = '';
      for (let j = 0; j < this.width; j++) {
        block += c;
      }
      console.log(block);
    }
  }
}

module.exports = Square;
