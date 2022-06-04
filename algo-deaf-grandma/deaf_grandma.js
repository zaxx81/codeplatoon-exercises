function deafGrandma() {
  let reply
  let goodbyeCount = 0
  let convo = prompt("Say something to Grandma?")
  
  while (convo != null) {
    if (convo === "") {
      reply = "WHAT?!"
    } else if (convo === "GOODBYE!") {
      if (goodbyeCount === 0) {
        reply = "LEAVING SO SOON?"
        goodbyeCount++
      } else {
        reply = "LATER, SKATER!"
        alert(`You said: ${convo} \nGrandma replied: ${reply}`)
        document.writeln("Program exited...")
        return
      }
    } else if (convo.toUpperCase() === convo) {
      reply = "NO, NOT SINCE 1946!"
    } else reply = "SPEAK UP, KID!"
    
    alert(`You said: ${convo} \nGrandma replied: ${reply}`)
    convo = prompt("Say something to Grandma?")
  }
  document.writeln("User selected to cancel. Program exited...")
  return
}

deafGrandma()