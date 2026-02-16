$(document).ready(function () {
    var allProducts = [];

    loadProducts();

    function loadProducts() {
        $.get(productListApiUrl, function (response) {
            if (response) {
                allProducts = response;
                displayProducts(allProducts);
            }
        });
    }

    function displayProducts(products) {
        var grid = $("#productGrid");
        grid.empty();

        if (products.length === 0) {
            grid.append('<div class="col-xs-12 text-center"><h4>No products found</h4></div>');
            return;
        }

        $.each(products, function (index, product) {
            var delay = index * 0.1; // Stagger animation

            // Simple logic to map product names to images
            var imagePath = 'https://via.placeholder.com/150';
            if (product.name.toLowerCase() === 'toothpaste') {
                imagePath = '/static/images/toothpaste.png';
            } else if (product.name.toLowerCase() === 'spinach') {
                imagePath = '/static/images/spinach.png';
            } else if (product.name.toLowerCase() === 'bread') {
                imagePath = '/static/images/bread.png';
            } else if (product.name.toLowerCase() === 'potato') {
                imagePath = '/static/images/potato.png';
            }

            var card = `
                <div class="col-md-3 col-sm-6 mb-4" style="opacity: 0; animation: fadeInUp 0.5s ease-out ${delay}s forwards;">
                    <div class="box-info text-center product-card" style="padding: 20px; transition: transform 0.2s;">
                        <div style="height: 150px; background: #fff; margin-bottom: 15px; border-radius: 4px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
                            <img src="${imagePath}" alt="${product.name}" style="max-height: 100%; max-width: 100%; object-fit: contain;" onerror="this.src='https://via.placeholder.com/150'">
                        </div>
                        <h3 style="margin: 10px 0; font-size: 18px; font-weight: 600;">${product.name}</h3>
                        <p class="text-muted" style="font-size: 14px; margin-bottom: 5px;">Unit: ${product.uom_name}</p>
                        <h4 class="text-primary" style="margin-bottom: 15px;">$${product.price_per_unit}</h4>
                        <button class="btn btn-primary btn-block add-btn-${product.product_id}" onclick="addToCart(${product.product_id}, '${product.name}', ${product.price_per_unit})">Add to Cart</button>
                    </div>
                </div>`;
            grid.append(card);
        });
    }

    // Search functionality
    $("#searchInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        var filteredProducts = allProducts.filter(function (product) {
            return product.name.toLowerCase().indexOf(value) > -1;
        });
        displayProducts(filteredProducts);
    });
});
