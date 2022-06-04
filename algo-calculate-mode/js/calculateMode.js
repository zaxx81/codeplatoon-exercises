exports.calculateMode = (arr) => {
  // Create an object of unique list values
  const results = []
  const keyValues = [...new Set(arr)]

  // Count the occurrences of unique values
  const keysCount = keyValues.map((elem) => {
    let count = arr.filter((item) => {
      return item === elem
    }).length
    
    return [elem, count]
  }).sort((a, b) => b[1] - a[1])
  
  // Return all values with greatest number of occurrences1
  let highestCount = keysCount[0][1]
  
  keysCount.map((elem) => {
    if (elem[1] === highestCount) results.push(elem[0])
  })

  return results
}