/**
 * A module that counts the characters in a string
 * @module charCount
 * @param  {string} str - input string
 * @returns {array} [<character>, <occurrences>]
 */
exports.charCount = function (str) {
  // Create an alphabetical array of unique alphabet characters in str
  const re = new RegExp(/[a-z]/, "g")
  const charsArr = [...new Set(str.toLowerCase()
    .match(re)
    .sort())]
  
  // Creates an array of [chars][count]
  const charsCountArr = charsArr.map((chars) => {
    const re = new RegExp(chars, "gi")
    const count = str.match(re).length
    return [chars, count]
  })

  // Sort results[char][count] by count in desending order
  const results = charsCountArr.sort((a, b) => b[1] - a[1])

  return results
}
