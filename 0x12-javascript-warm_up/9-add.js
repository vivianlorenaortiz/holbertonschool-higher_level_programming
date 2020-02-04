#!/usr/bin/node
add(parseInt(process.argv[2]), parseInt(process.argv[3]));

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
