exports.factorial = function(num) {
  let inputNum = num
  let result = 1
    
  for( inputNum; inputNum > 0; inputNum-- ) {
    result *= inputNum
  }
  return result
};
