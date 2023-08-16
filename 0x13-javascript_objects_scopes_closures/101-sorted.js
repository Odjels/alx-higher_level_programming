#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const keys in dict) {
  if (newDict[dict[keys]]) {
    newDict[dict[keys]].push(keys);
  } else {
    newDict[dict[keys]] = [keys];
  }
}

console.log(newDict);
