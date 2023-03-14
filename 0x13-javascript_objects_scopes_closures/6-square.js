#!/usr/bin/node
const Psquare = require('./5-square.js');
module.exports = class Square extends Psquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let emp = '';
        for (let j = 0; j < this.size; j++) {
          emp += c;
        }
        console.log(emp);
      }
    }
  }
};
