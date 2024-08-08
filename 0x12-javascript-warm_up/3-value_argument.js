#!/usr/bin/node
// a script that prints the first argument passed to it

let count = 0;
while (process.argv[count]) {
  count++;
}

if (count <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
