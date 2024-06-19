#!/usr/bin/node
// a script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:

const n = Number(process.argv[2]);
if (n) {
  Math.floor(n);
  console.log('My number:', n);
} else {
  console.log('Not a number');
}
