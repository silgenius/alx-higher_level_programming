#!/usr/bin/node
//  a script that prints the addition of 2 integers

function add (a, b) {
  return (a + b);
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
console.log(add(a, b));
