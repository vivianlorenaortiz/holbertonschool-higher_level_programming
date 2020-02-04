#!/usr/bin/node
exports.callMeMoby = function (n, nfunction) {
  for (let i = 0; i < n; i++) {
    nfunction();
  }
};
