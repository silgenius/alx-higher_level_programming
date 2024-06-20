#!/usr/bin/node
// a function that executes x times a function.

function addMeMaybe(number, theFunction) {
    theFunction(number + 1);
  }
}

module.exports = {
  addMeMaybe
};
