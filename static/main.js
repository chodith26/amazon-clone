fetch('/api/products')
    .then(response => response.json())
    .then(products => {
        const grid = document.getElementById('js-products-grid');
        products.forEach(product => {
            const card = document.createElement('div');
            card.classList.add('rec-card');
            card.innerHTML = `
                <p class="rec-name">${product.name}</p>
                <p class="rec-price">${product.price}</p>
                <span class="rec-category">${product.category}</span>
            `;
            grid.appendChild(card);
        });
    })
    .catch(error => console.error('Fetch error:', error));