/**
 * @param  {} valueToFind
 * @param  {} arrayToSearchThrough
 */
exports.linearSearch = function(valueToFind, arrayToSearchThrough) {
  let result
  let len = arrayToSearchThrough.length
  for (let i = 0; i < len; i++) {
      if (valueToFind === arrayToSearchThrough[i]) {
        result = i
      }
  }
  return result
}

exports.linearSearchGlobal = function(valueToFind, arrayToSearchThrough) {
    let result = []
    let len = arrayToSearchThrough.length
    for (let i = 0; i < len; i++) {
        if (valueToFind === arrayToSearchThrough[i]) {
          result.push(i)
        }
    }
    return result
}