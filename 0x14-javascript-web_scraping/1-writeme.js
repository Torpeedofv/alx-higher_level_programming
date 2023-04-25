#!/usr/bin/node
const arg = process.argv.slice(2);
const fs = require('fs');
try {
  fs.writeFileSync(arg[0], arg[1]);
} catch (err) {
  console.error(err);
}
