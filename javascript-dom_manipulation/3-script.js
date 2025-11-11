#!/usr/bin/node
const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');
toggleHeader.addEventListener('click', function () {
  header.classList.replace('red', 'green') ||
    header.classList.replace('green', 'red');
});
