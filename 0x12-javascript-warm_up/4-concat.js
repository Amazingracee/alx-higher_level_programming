#!/usr/bin/node

const argc = process.argv;
if (argc === 3) {
  console.log(`${argc[2]} is ${argc[3]}`);
} else if (argc === 2) {
  console.log(`${argc[2]} is ${argc[3]}`);
} else {
  console.log(`${argc[2]} is ${argc[3]}`);
}
