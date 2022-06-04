exports.creditCheck = function(str) {

    let numArr = str.split('').map(Number)
    
    let len = numArr.length-1
    
    for (let i = 0; i < len; i++){
        if (i % 2 === 0){
            numArr[i] *= 2
            if(numArr[i] > 9) {
                numArr[i] -= 9
            }
        }
    }
    let sums = numArr.reduce((total, elem) => {
        return total + elem
    })
    if (sums % 10 === 0) {
        return "The number is valid!"
    } else {
        return "The number is invalid!"
    }
}