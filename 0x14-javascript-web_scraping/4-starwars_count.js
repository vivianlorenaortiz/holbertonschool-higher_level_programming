#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (let i = 0; i < JSON.parse(body).count; i++) {
      const characters = (JSON.parse(body).results[i].characters);
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
