#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterID = 18;
let count = 0;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmsData = JSON.parse(body);
    count = filmsData.results.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`)).length;
    console.log(count);
  } else {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
  }
});
