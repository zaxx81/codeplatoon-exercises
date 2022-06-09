let test = require('./bubbleSort')
let seArr = require('shallow-equal/arrays')

console.log(seArr(test.bubbleSort([4, 3, 5, 0, 1]), [0, 1, 3, 4, 5]))
console.log(seArr(test.bubbleSort([1, 3, 5, 9, 4, 6, 2, 0, 8, 7]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
console.log(seArr(test.bubbleSort([227, 605, 201, 653, 592, 545, 663, 316, 732, 849, 206, 580, 961, 253, 810, 536, 481, 325, 626, 384]), [201, 206, 227, 253, 316, 325, 384, 481, 536, 545, 580, 592, 605, 626, 653, 663, 732, 810, 849, 961]))