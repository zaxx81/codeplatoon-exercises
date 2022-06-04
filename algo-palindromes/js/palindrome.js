exports.palindrome = function(word) {
  // Create two compare strings, 1st one is first half of word, and second one is seconf half of word reverse. Need to consider if word is odd or even.
  const re = new RegExp(/[a-z0-9]/, 'g')
  const charsArr = String(word).toLowerCase().match(re)
  let len = charsArr.length
  let middleIdx = parseInt(len / 2)
  
  // If word length is odd, remove middle
  if ((len % 2) === 1) {
    charsArr.splice(middleIdx, 1)
    len = charsArr.length
  }
  // let compareString1, compareString2
  let compareString1 = charsArr.slice(0,middleIdx).join('')
  let compareString2 = charsArr.slice(middleIdx)
    .reverse()
    .join('')

  // Return the comparison of the two strings
  return compareString1 === compareString2
}
