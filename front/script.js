document.addEventListener("DOMContentLoaded", () => {
    const productGrid = document.getElementById('product-grid');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    const pageIndicator = document.getElementById('page-indicator');

    let currentPage = 1;
    const limit = 24; 

    async function fetchProducts(page) {
        try {
            const response = await fetch(`http://localhost:8080/products?page=${page}&limit=${limit}`);
            if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);

            const data = await response.json();
            renderProducts(data.products);

            currentPage = page;
            pageIndicator.textContent = `Page ${currentPage}`;

            prevButton.disabled = currentPage === 1;
            nextButton.disabled = data.products.length < limit; 
        } catch (error) {
            console.error('Erreur lors de la récupération des produits :', error);
        }
    }

    function renderProducts(products) {
        productGrid.innerHTML = ''; 
        products.forEach((product) => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';
            productCard.innerHTML = `
                <img src="${product.image_url}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p class="price">${product.price}</p>
            `;
            productGrid.appendChild(productCard);
        });
    }

    prevButton.addEventListener('click', () => {
        if (currentPage > 1) fetchProducts(currentPage - 1);
    });

    nextButton.addEventListener('click', () => {
        fetchProducts(currentPage + 1);
    });

    fetchProducts(currentPage);
});
