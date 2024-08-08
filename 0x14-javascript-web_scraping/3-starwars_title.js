#!/usr/bin/node
/* a script that prints the title of a Star Wars movie where the
episode number matches a given integer. */

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  console.log(body.title);
});
