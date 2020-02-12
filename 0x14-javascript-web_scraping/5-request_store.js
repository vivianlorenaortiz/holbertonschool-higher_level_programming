#!/usr/bin/node

let request = require('request');
let fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf-8');
  } catch (err) {

  }
});
