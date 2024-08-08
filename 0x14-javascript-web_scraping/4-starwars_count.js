#!/usr/bin/node
/* a script that prints the number of movies where the
character “Wedge Antilles” is present */

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  const x = 0;
  const y = 0;
  let count = 0;
  while (body.results[x]) {
    while (body.results[x].characters[y]) {
      text = body.results[x].characters[y];
      if (text.match('18')) {
        count += 1;
        break;
      }
    }
  }
  console.log(count);
});
