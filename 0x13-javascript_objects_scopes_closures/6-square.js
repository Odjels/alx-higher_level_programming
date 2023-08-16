#!/usr/bin/node
/* create a class square which inherits from rectangle */
const oldSqaure = require('./5-square');

class Square extends oldSqaure {
  charPrint (c) {
    let k = c;
    if (!c) {
      k = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(k.repeat(this.width));
    }
  }
}

module.exports = Square;
