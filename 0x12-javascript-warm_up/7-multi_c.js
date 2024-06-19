#!/usr/bin/node
//  a script that prints x times “C is fun”

let n = Number(process.argv[2]);
Math.floor(n);

if (n) {
  while (n > 0) {
    console.log('C is fun');
    n--;
  }
} else {
  console.log('Missing number of occurrences');
}
