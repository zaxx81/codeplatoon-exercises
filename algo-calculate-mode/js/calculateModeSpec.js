let test = require('./calculateMode')
let seArr = require('shallow-equal/arrays')

console.log(seArr(test.calculateMode([4.5, 0, 0]), [0]))
console.log(seArr(test.calculateMode([1.5, -1, 1, 1.5]), [1.5]))
console.log(seArr(test.calculateMode([1,2,3,3]), [3]))
console.log(seArr(test.calculateMode([1,1,2,2]), [1, 2]))
console.log(seArr(test.calculateMode([1,2,3]), [1, 2, 3]))
console.log(seArr(test.calculateMode(["who", "what", "where", "who"]), ["who"]))
