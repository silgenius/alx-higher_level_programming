#!/usr/bin/node

const fs = require('fs');
// F_file = require(`./${process.argv[2]}`);
// S_file = require(`./${process.argv[3]}`);

const Fdata = fs.readFileSync(`./${process.argv[2]}`, 'utf-8');
const Sdata = fs.readFileSync(`./${process.argv[3]}`, 'utf-8');

fs.writeFileSync(`./${process.argv[4]}`, `${Fdata}${Sdata}`, 'utf-8');
