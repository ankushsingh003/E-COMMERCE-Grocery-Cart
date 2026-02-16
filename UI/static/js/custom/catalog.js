$(document).ready(function () {
    loadProducts();

    function loadProducts() {
        $.get(productListApiUrl, function (response) {
            if (response) {
                var grid = $("#productGrid");
                grid.empty();
                $.each(response, function (index, product) {
                    var card = `
                        <div class="col-md-3 col-sm-6 mb-4">
                            <div class="box-info text-center product-card" style="padding: 20px; transition: transform 0.2s;">
                                <div style="height: 150px; background: #e9ecef; margin-bottom: 15px; border-radius: 4px; display: flex; align-items: center; justify-content: center;">
                                    <i class="zmdi zmdi-image zmdi-hc-4x text-muted"></i>
                                </div>
                                <h3 style="margin: 10px 0; font-size: 18px; font-weight: 600;">${product.name}</h3>
                                <p class="text-muted" style="font-size: 14px; margin-bottom: 5px;">Unit: ${product.uom_name}</p>
                                <h4 class="text-primary" style="margin-bottom: 15px;">$${product.price_per_unit}</h4>
                                <button class="btn btn-primary btn-block" onclick="addToCart(${product.product_id}, '${product.name}', ${product.price_per_unit})">Add to Cart</button>
                            </div>
                        </div>`;
                    grid.append(card);
                });
            }
        });
    }
});
