var sp = require("./sumPairs");

console.log(sp.sumPairs([1,2,3,4,5], 9))  //[[4,5]]
console.log(sp.sumPairs([1,2,3,4,5], 7) )  // [[2,5], [3,4]]
console.log(sp.sumPairs([3, 1, 5, 8, 2], 27))  // 'unable to find pairs'