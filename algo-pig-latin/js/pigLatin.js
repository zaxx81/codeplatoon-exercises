exports.translate = function(word) {
  const result = []
  let strList = word.split(' ')

  for (let word of strList) {
    let capitalWord = false
    let wordBuffer = ''
    let punctuationBuffer = ''
    // Checks if first letter is capitalized
    if (word[0].toUpperCase() === word[0]) {
      capitalWord = true
    }

    // Checks if word contains a new line \n
    if (/\n/.test(word)) {
      
    }

    // Checks if the last char is punctuation (, . ? !)
    if (/[^a-z]$/i.test(word)) {
      end = word.length
      punctuationBuffer = word[end - 1]
      word = word.substring(0, end - 1)
    }

    // Changes word to all lowercase
    word = word.toLowerCase()
    // Starts with a vowel
    if (/^[aeiou]/i.test(word)) {
      wordBuffer = (word.concat('ay'))
    }
    // Starts with qu
    else if ( /^(qu)/i.test(word)){
      wordBuffer = (word.substr(2).concat(word.substr(0, 2), 'ay'))
    }
    // Starts with a consonant then qu
    else if ( /^[^aeiou](qu)/i.test(word)){
      wordBuffer = (word.substr(3).concat(word.substr(0, 3), 'ay'))
    }
    // Starts with four consonants
    else if ( /^[^aeiou]{4}/i.test(word)){
      wordBuffer = (word.substr(4).concat(word.substr(0, 4), 'ay'))
    }
    // Starts with three consonants
    else if ( /^[^aeiou]{3}/i.test(word)){
      wordBuffer = (word.substr(3).concat(word.substr(0, 3), 'ay'))
    }
    // Starts with two consonants
    else if ( /^[^aeiou]{2}/i.test(word)){
      wordBuffer = (word.substr(2).concat(word.substr(0, 2), 'ay'))
    }
    // All others
    else {
      wordBuffer = (word.substr(1).concat(word.substr(0, 1), 'ay'))
    }
    if (capitalWord == true) {
      wordBuffer = wordBuffer.substr(0,1).toUpperCase().concat(wordBuffer.substring(1))
    }
    
    // Send punctuation (, . ? !) to the end of the new word
    if (punctuationBuffer != '')
    wordBuffer += punctuationBuffer

    result.push(wordBuffer)
  }
  
  console.log(result.join(' '))

  return result.join(' ')
};
