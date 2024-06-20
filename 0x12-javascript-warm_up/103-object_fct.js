#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

const incr = function() {
  this.value += 1;
  this.incr = [Function];
}
myObject.incr = incr;
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
