#!/usr/bin/node
const addList = document.querySelector('#add_item');
addList.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  const myList = document.querySelector('ul.my_list');
  myList.appendChild(newItem);
});
