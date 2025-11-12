#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
const trad = document.querySelector('#hello');
fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then((response) => response.json())
  .then((data) => {
    trad.textContent = data.hello;
  })
  .catch((error) => console.error('Error:', error));
});