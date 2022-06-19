/* DOM Variables */
let form = document.getElementById('addForm')
let itemList = document.getElementById('items')
let filter = document.getElementById('filter')
let clear = document.getElementById('clear-filter')

/* Event Listeners */
form.addEventListener('submit', addItem)
itemList.addEventListener('click', completeItem)
itemList.addEventListener('click', removeItem)
filter.addEventListener('keyup', filterItems)
clear.addEventListener('click', clearFilter)

/* Functions */

// Add Item Function
function addItem(e) {
  e.preventDefault()

  // Get the input value from the event
  let newItem = document.getElementById('item').value

  // Create a new <li> with input
  let newLi = document.createElement('li')
  newLi.className = 'list-group-item'
  newLi.appendChild(document.createTextNode(newItem))

  // Create the delete icon
  let newDelIcon = document.createElement('i')
  newDelIcon.className = 'bi-trash float-end'
  newLi.appendChild(newDelIcon)

  // Create the complete icon
  let newCompIcon = document.createElement('i')
  newCompIcon.className = 'bi-check-square-fill float-end pe-1'
  newLi.appendChild(newCompIcon)

  itemList.appendChild(newLi)
}

// Complete Item Function
function completeItem(e) {
  if (e.target.classList.contains('bi-check-square-fill')) {
    if (e.target.parentElement.firstChild.data == 'Code') {
      alert("Coding is never finished!")
    } else {
      if (e.target.parentElement.classList.contains('text-decoration-line-through')) {
        e.target.parentElement.classList.remove('text-decoration-line-through')
      }
      else {
        e.target.parentElement.classList.add('text-decoration-line-through')
      }
    }
  }
}

// Remove Item Function
function removeItem(e) {
  if (e.target.classList.contains('bi-trash')) {
    if (e.target.parentElement.firstChild.data == 'Code') {
      alert("Coding is never finished!")
    } else {
      if (confirm('Are you sure?')) {
        let li = e.target.parentElement
        itemList.removeChild(li)
      }
    }
  }
}

// Filter Function
function filterItems(e) {
  // Adds a clear filter button
  clear.style.display = 'block'

  // Convert filter text to lowercase
  let text = e.target.value
  let items = itemList.getElementsByTagName('li')
  // Convert Items from HTML Collection to an Array
  Array.from(items).forEach( (item) => {
    let itemName = item.firstChild.textContent
    let re = new RegExp(text, 'gi')
    if (re.test(itemName)) {
      item.style.display = 'block'
    } else {
      item.style.display = 'none'
    }
  })
}

// Clear Filter Function
function clearFilter(e) {
  if (e.target.classList.contains('bi-x-lg')) {
    filter.value = ""
    clear.style.display = 'none'
    
    let items = itemList.getElementsByTagName('li')
    Array.from(items).forEach( (item) => {
      item.style.display = 'block'
    })
  }
}