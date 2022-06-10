exports.translate = function(word) {
  const result = []
  let strList1 = word.split('\n')
  let strList2 = []
  let strList = []
  
  // Handles newline character
  if (strList1.length > 1) {
    for (let i = 0; i < strList1.length; i++) {
      strList2.push(strList1[i])
      strList2.push('\n')
      }
    if (strList2[strList2.length-1] === '\n') {
      strList2.pop()
    }
    strList1 = [...strList2]
  }
  // Splits on spaces
  for (let elem of strList1) {
    strList.push(elem.split(' '))
  }
  // Checks first letter and ending punctuation
  for (let elem of strList) {
    for (let word of elem) {
      let capitalWord = false
      let wordBuffer = ''
      let punctuationBuffer = ''
      
      // Checks if word is a newline
      if (word === '\n') {
        result.push(word)
        break
      }
      // Checks if first letter is capitalized
      if (word[0].toUpperCase() === word[0]) {
        capitalWord = true
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
  }
  
  let returnStr = ''
  for (let i = 0; i < result.length; i++) {
    if (i == result.length - 1 || result[i] == '\n') {
      returnStr += result[i]
    } else {
      returnStr += result[i]
      returnStr += ' '
    }
  }

  return returnStr
};
