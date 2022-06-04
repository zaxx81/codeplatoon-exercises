const fibonacci = (num) => {
    
    const fibNums = [0, 1]
    let fn = 0
    
    if (num === 0) {
      return 0
    } else if (num === 1) {
      return 1
    } else {
      for( let i = 2; i <= num; i++ ) {
        fn = fibNums[i-1] + fibNums[i-2]
        fibNums.push(fn)
      }
    }

    return fibNums[fibNums.length - 1]
}

module.exports = {fibonacci}