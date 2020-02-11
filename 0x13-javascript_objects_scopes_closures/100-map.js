#!/usr/bin/node

const numbers = require('./100-data').list;

const multipleByIndex = numbers.map(function (x, idx) {
  return x * idx;
});

console.log(numbers);
console.log(multipleByIndex);
