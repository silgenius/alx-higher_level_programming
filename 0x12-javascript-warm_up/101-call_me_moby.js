#!/usr/bin/node
// a function that executes x times a function.

function executeFunc(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}

module.exports = executeFunc;
