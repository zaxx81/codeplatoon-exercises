function bottleSong() {
  let n = 99

  while( n >= 0) {
    if( n > 2) {
      console.log(`${n} bottles of beer on the wall, ${n} bottles of beer.
Take one down and pass it around, ${n - 1} bottles of beer on the wall.`)
    } else if( n === 2 ) {
      console.log(`2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.`)
    } else if( n === 1 ) {
      console.log(`1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.`)
    } else if( n === 0 ) {
      console.log(`No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.`)
    }
    
    n--
  }
}

bottleSong()