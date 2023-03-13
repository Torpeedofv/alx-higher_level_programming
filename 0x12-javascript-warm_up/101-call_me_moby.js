#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let newFunc = '';
  while (x > 0) {
    x--;
    newFunc += `${theFunction()}\n`;
  }
  return newFunc;
};
