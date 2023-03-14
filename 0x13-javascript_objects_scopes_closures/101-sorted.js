#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {}
for (let [key, value] of Object.entries(dict)) {
    if (!newDict[value]) {
        newDict[value] = [];
    }
    newDict[value].push(key);
    }
console.log(newDict)
console.log(dict)