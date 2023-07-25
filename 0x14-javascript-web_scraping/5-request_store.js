#!/usr/bin/node

const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
