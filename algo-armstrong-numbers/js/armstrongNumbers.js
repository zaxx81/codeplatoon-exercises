// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(num) {

  // armstrongArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

  // split number into individual digits
  // take digits to the power of number of digits
  // add the sum together and see if equal to input number
  
  let results = []
  
  for(let i = 0; i < num; i++) {

      let numStr = String(i)
      let splitNum = numStr.split('')

      let digits = splitNum.length

      let sumDigPow = splitNum.reduce(digiPow, 0)
      
      function digiPow(total, elem) {
          return total + Number(elem) ** digits
  
      }

      if (sumDigPow === i) {
          results.push(i)
      }
  }
  return results
};