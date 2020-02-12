#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf-8');
  } catch (err) {

  }
});
