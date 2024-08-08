#!/usr/bin/node
const { dict } = require('./101-data.js');

let value = Object.values(dict);
const key = Object.keys(dict);
value = [...new Set(value)].sort((a, b) => b + a);
const myObject = {};

let i = 0;
while (value[i]) {
  let j = 0;
  myObject[value[i]] = [];
  while (dict[key[j]]) {
    if (dict[key[j]] === value[i]) {
      myObject[value[i]].push(key[j]);
    }
    j++;
  }
  i++;
}

console.log(myObject);
