#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (((w <= 0) || (w === undefined)) || ((h <= 0) || (h === undefined))) {
      return constructor.name + {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let ex = '';
      for (let j = 0; j < this.width; j++) {
        ex += 'X';
      }
      console.log(ex);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
