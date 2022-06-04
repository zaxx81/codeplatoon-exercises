balanceParens = (str) => {
  let result = str.split('')
  result = matchPairs([...result], '(', ')').reverse()
  result = matchPairs([...result], ')', '(').reverse()

  return result.join('')
}

function matchPairs(arr, openChar, closeChar) {
  let result = [] 
  let matchCount = 0
  
  arr.forEach(char => {
    if (char === openChar) {
      result.push(char)
      matchCount ++
    }
    if (char === closeChar) {
      if (matchCount > 0) {
        result.push(char)
        matchCount --
      }
    }
    if (char !== openChar && char != closeChar) {
      result.push(char)
    }
  })
  
  return result
}

module.exports = { balanceParens }