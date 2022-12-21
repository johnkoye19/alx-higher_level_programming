#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method print
  print () {
    let post = '';
    for (let i = 0; i < this.width; i++) {
      post = post + 'X';
    }
    for (let a = 0; a < this.height; a++) {
      console.log(post);
    }
  }
}

module.exports = Rectangle;
