#!/usr/bin/node

const id = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/:id' + id;
const request = require('request');

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Error Code:' + response.statusCode);
  }
});
