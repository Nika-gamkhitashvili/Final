let cardsArea = document.querySelector('section');
let apiUrl = "https://fakestoreapi.com/products"

fetch(apiUrl)
.then(response => response.json())
