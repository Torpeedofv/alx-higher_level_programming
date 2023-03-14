#!/usr/bin/node
const Psquare = require('./5-square.js');
module.exports = class Square extends Psquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let emp = '';
        for (let j = 0; j < this.width; j++) {
          emp += c;
        }
        console.log(emp);
      }
    }
  }
};
