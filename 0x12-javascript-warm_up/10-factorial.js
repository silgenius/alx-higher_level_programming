#!/usr/bin/node
//  a script that computes and prints a factorial

function factorial (n) {
  if (!n) { return (1); }
  if (n === 0) { return (1); }

  return (n * factorial(n - 1));
}

const n = Number(process.argv[2]);
console.log(factorial(n));
