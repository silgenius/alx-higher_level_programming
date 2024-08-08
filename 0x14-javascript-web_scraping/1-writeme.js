#!/usr/bin/node
/* a script that writes a string to a file. */

const fs = require('fs');
const fileContent = process.argv[3];
const fileName = process.argv[2];

fs.writeFile(fileName, fileContent, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
