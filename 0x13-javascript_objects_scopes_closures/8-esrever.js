#!/usr/bin/node

exports.esrever = function (list) {
  let count = list.length - 1;
  const newList = [];
  while (count >= 0) {
    newList.push(list[count]);
    count--;
  }
  return (newList);
};
