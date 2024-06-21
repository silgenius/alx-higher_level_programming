#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let block = '';
      for (let j = 0; j < this.size; j++) {
        c ? block += c : block += 'X';
      }
      console.log(block);
    }
  }
}

module.exports = Square;
