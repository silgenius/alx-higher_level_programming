#!/usr/bin/node
const { list } = require('./100-data');

console.log(list);
const newList = list.map((x, index) => x * index);
console.log(newList);
