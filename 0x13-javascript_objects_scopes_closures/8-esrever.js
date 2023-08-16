#!/usr/bin/node

exports.esrever = function (list) {
  const listLength = list.length;
  const newList = [];
  let g = 0;

  for (let a = listLength - 1; a >= 0; a--) {
    newList[g++] = list[a];
  }
  return (newList);
};
