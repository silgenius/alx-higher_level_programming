#!/usr/bin/node
/* a script that reads and prints the content of a file. */

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }

  console.log(data);
});
