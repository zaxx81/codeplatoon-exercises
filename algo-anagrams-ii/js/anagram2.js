exports.anagramsFor = function(word, listOfWords) {
    let results = []
    let compareWord = word.toLowerCase().split('').sort().join('')
    let compareListOfWords = listOfWords.map(elem => {
        return elem.toLowerCase().split('').sort().join('')
        })
    
    for (let i = 0; i < compareListOfWords.length; i++) {
        if (compareWord === compareListOfWords[i]) {
            results.push(listOfWords[i])
        }
    }

    return results
}