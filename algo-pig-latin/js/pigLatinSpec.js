// Rewrite this in Unit Test

var pig = require("./pigLatin");

console.log("translates a word beginning with a vowel:");
console.log(pig.translate("apple") === "appleay");
console.log("translates a word beginning with a consonant:");
console.log(pig.translate("banana") === "ananabay");
console.log("translates a word beginning with two consonants:");
console.log(pig.translate("cherry") === "errychay");
console.log("translates two words:");
console.log(pig.translate("eat pie") === "eatay iepay");
console.log("translates a word beginning with three consonants:");
console.log(pig.translate("three") === "eethray");
console.log("counts 'sch' as a single phoneme:");
console.log(pig.translate("school") === "oolschay");
console.log("counts 'qu' as a single phoneme:");
console.log(pig.translate("quiet") === "ietquay");
console.log("counts 'qu' as a consonant even when it's preceded by a consonant:");
console.log(pig.translate("square") === "aresquay");
console.log("translates many words:");
console.log(pig.translate("the quick brown fox") === "ethay ickquay ownbray oxfay");

console.log(pig.translate("I go to Apple University") === 'Iay ogay otay Appleay Universityay')

console.log(pig.translate("I go to the University of Maryland") === 'Iay ogay otay ethay Universityay ofay Arylandmay')

console.log(pig.translate("Hi, I'm Zack") === "Ihay, I'may Ackzay")

console.log('\n-Compare output manually-\n')
console.log(pig.translate("Hi, I'm Zack.\nHow are you?"))
console.log("\nShould looke like this:\n\nIhay, I'may Ackzay.\nOwhay areay ouyay?\n")
