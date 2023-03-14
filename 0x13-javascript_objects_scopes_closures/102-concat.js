#!/usr/bin/node
const arg = process.argv.slice(2);
const fs = require('fs')
let file1 = fs.readFileSync(arg[0], 'utf8')
let file2 = fs.readFileSync(arg[1], 'utf8')
fs.writeFileSync(arg[2], file1 + file2)