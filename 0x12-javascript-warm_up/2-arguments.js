#!/usr/bin/node

const arg = process.argv;

// trying to get the num of argments
const num = arg.length - 1;

if (num === 2) {
  console.log('Argument found');
} else if (num > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
