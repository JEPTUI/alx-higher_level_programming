#!/usr/bin/node

const id = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], (err, response, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
