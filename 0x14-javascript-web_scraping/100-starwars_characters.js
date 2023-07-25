#!/usr/bin/node

const id = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    for (const i in movie.characters) {
      request(movie.characters[i], (err, response, body) => {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
