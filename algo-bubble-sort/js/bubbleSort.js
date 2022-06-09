exports.bubbleSort = function(arr) {
  const results = [...arr]
  let swaps = 0
  let pass_swap = false
  let lastIdx = results.length

  for (let i = 0; i < lastIdx; i++ ) {
    for (let j = 0; j < lastIdx - 1; j++) {
      if (results[j] > results[j + 1]) {
        pass_swap = true
        swaps ++
        let temp = results[j]
        results[j] = results[j + 1]
        results[j + 1] = temp
      }
    }
    if (!pass_swap) {
      return
    }
  }
  console.log(`Final result: ${results}`)
  console.log(`Swaps: ${swaps}`)

  return results
}
