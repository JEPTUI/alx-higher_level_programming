#!/usr/bin/node
const fs = require('fs');

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
let dataA = fs.readFileSync(fileA, 'utf8');
let dataB = fs.readFileSync(fileB, 'utf8');
const combinedData = (dataA + dataB);
fs.writeFileSync(fileC, combinedData);
