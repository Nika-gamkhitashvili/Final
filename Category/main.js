
let cardsArea = document.querySelector('section');
let apiUrl = "https://fakestoreapi.com/products"

fetch(apiUrl)
.then(response => response.json())
.then(product => htmlRenderer(product))

function htmlRenderer(productList) {
    console.log(productList)

    productList.forEach(product => {
        cardsArea.innerHTML +=
        `<div class="card" style="width: 18rem; margin:50px;">
         <img class="card-img-top" src="${product.image}" alt="...">
          <div class="card-body">
          <h5 class="card-title">${product.title}</h5>
          <p class="card-text">${product.background}</p>
          <a href="${product.url}" class="btn btn-primary">see info</a>
       </div>
      </div>`
    
     })
    }





