#!/usr/bin/node

const arg = process.argv;

// trying to get the num of argments
let num = 0;
for (const x in arg) {
  num = num + 1;
}

if (num > 2) {
  console.log(arg[2]);
} else {
  console.log('No argument');
}
