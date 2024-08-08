#!/usr/bin/node
// a script that prints a square

const n = Number(process.argv[2]);
Math.floor(n);

let x = n;
let y = 0;
let block;

if (n) {
  while (x > 0) {
    block = '';
    while (y !== n) {
      block += 'X';
      y++;
    }
    console.log(block);
    y = 0;
    x--;
  }
} else {
  console.log('Missing size');
}
