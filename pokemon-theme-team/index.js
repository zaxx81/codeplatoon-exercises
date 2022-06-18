console.log("Let's Catch a Pokemon!")
const catchButton = document.querySelector('.catchButton')
const centerState = document.getElementById('centerStage')

const getMon = async () => {
  const pokemonURL = "https://pokeapi.co/api/v2/pokemon"
  let limit = '?limit=1'
  let response = await axios.get(pokemonURL + limit)
  let count = response.data.count
  limit = `?limit=${count}`
  console.log(`Number of Pokemon: ${count}`)

  // Pokemon Array. Each element contains 'name' and 'url'
  response = await axios.get(pokemonURL + limit)
  const pokemonData = response.data.results

  // Setup for myPokemonDiv
  const randomIndex = Math.floor(Math.random() * (count - 1))
  const randomPokemon = pokemonData[randomIndex]

  response = await axios.get(randomPokemon.url)
  const myPokemon = response.data
  console.log(myPokemon)
  console.log(myPokemon.id)
  console.log(myPokemon.name)
  
  let img = document.createElement('img')
  img.src = myPokemon.sprites.front_default
  img.alt = 'My Pokemon'
  
  centerState.innerHTML = ""
  centerState.append(img)

  // Get 5 more pokemon

  // Create Carousel with all the pokemon


}

catchButton.addEventListener('click', getMon)