/* DOM Variables */
const form = document.getElementById('addForm')
const draggableList = document.getElementById('draggable-list')
const filter = document.getElementById('filter')
const clear = document.getElementById('clear-filter')
const itemTextField = document.getElementById('item')

const toDoItems = ['Eat', 'Sleep', 'Code']
const listItems = [];
let dragStartIndex;
createList()

/* Event Listeners */
form.addEventListener('submit', addItem)
draggableList.addEventListener('click', completeItem)
draggableList.addEventListener('click', removeItem)
filter.addEventListener('keyup', filterItems)
clear.addEventListener('click', clearFilter)

/* Functions */

// Add Item Function
function addItem(e) {
  e.preventDefault()
  let item = itemTextField.value
  let index = toDoItems.length
  toDoItems.push(item)
  
  const listItem = document.createElement('li')
  listItem.className = 'list-group-item'
  listItem.setAttribute('data-index', index)
  listItem.innerHTML = `
    <div class="draggable" draggable="true">
      <spand class="item-description">${item}</spand>
      <i class="bi-trash float-end"></i>
      <i class="bi-check-square-fill float-end pe-1"></i>
    </div>
  `
  listItems.push(listItem)
  draggableList.appendChild(listItem)
  document.getElementById('item').value = ""
}

// Complete Item Function
function completeItem(e) {
  if (e.target.classList.contains('bi-check-square-fill')) {
    if (e.target.previousElementSibling.previousElementSibling.textContent.toLowerCase() == 'code') {
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
    if (e.target.previousElementSibling.textContent.toLowerCase() == 'code') {
      alert("Coding is never finished!")
    } else {
      if (confirm('Are you sure?')) {
        let listItem = e.target.parentElement.parentElement
        draggableList.removeChild(listItem)
      }
    }
  }
}

// Filter Function
function filterItems(e) {
  // Adds a clear filter button
  clear.style.display = 'block'
  console.log(e)
  // Convert filter text to lowercase
  let text = e.target.value
  let items = draggableList.getElementsByTagName('li')
  // Convert Items from HTML Collection to an Array
  Array.from(items).forEach( (item) => {
    
    let itemName = item
      .getElementsByClassName('item-description')[0]
      .textContent
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
    
    let items = draggableList.getElementsByTagName('li')
    Array.from(items).forEach( (item) => {
      item.style.display = 'block'
    })
  }
}

function createList() {
  [...toDoItems].forEach( (item, index) => {
    const listItem = document.createElement('li')
    listItem.className = 'list-group-item'
    listItem.setAttribute('data-index', index)
    listItem.innerHTML = `
      <div class="draggable" draggable="true">
        <span class="item-description">${item}</span>
        <i class="bi-trash float-end"></i>
        <i class="bi-check-square-fill float-end pe-1"></i>
      </div>
    `
    listItems.push(listItem)
    draggableList.appendChild(listItem)
  })
}