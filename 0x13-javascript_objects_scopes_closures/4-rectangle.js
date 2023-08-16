#!/usr/bin/node
/* define a class rectangle with
properties of w and h
If w or h is equal to 0 or not a positive integer,
create an empty object
create a print method to return a rectangle
create a method to rotate the sides of a rectangle
create a method to double the sides */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const d = this.height;
    this.height = this.width;
    this.width = d;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
