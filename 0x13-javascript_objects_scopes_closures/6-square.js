#!/usr/bin/node
const Square5 = require('./5-square.js');

class Square extends Square5 {
  constructor(size) {
    super(size);
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
