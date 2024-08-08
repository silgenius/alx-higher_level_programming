#!/usr/bin/node
const Square5 = require('./5-square.js');

class Square extends Square5 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
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
