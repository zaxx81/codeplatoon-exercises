exports.isCharacterMatch = function(string1, string2) {
    let compareString1 = string1
        .split(' ').join('') // Removes spaces
        .toLowerCase().split('').sort().join('') // Makes lowercase and sorts
    let compareString2 = string2
        .split(' ').join('') // Removes spaces
        .toLowerCase().split('').sort().join('') // Makes lowercase and sorts
    
    return compareString1 === compareString2
}
