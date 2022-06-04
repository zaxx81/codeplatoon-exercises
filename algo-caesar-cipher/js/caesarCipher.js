exports.caesarCipher = function(str, shift) {
  
  const letterShift = (letter, shift, offset) => {
    return String.fromCharCode(
      ((letter.charCodeAt() - offset + shift + 26) % 26) + offset
    );
  }
  
  return str
    .replace( /[A-Z]/g, (match) => letterShift(match, shift, 65) )
    .replace( /[a-z]/g, (match) => letterShift(match, shift, 97) )
}
