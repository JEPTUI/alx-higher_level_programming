#!/usr/bin/node

const id = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode !== 200) {
    console.log('Error Code:' + response.statusCode);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
