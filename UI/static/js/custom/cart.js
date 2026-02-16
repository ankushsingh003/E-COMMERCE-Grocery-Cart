var cart = JSON.parse(localStorage.getItem('cart')) || [];

function updateCartCount() {
    var count = cart.reduce((acc, item) => acc + item.qty, 0);
    $("#cartCount").text(count);
}

function addToCart(id, name, price) {
    // Price might be string or number, ensure number
    price = parseFloat(price);

    var item = cart.find(i => i.id === id);
    if (item) {
        item.qty++;
    } else {
        cart.push({ id: id, name: name, price: price, qty: 1 });
    }
    saveCart();

    // Animation and feedback
    var btn = $(`.add-btn-${id}`);
    var originalText = btn.text();

    btn.addClass('btn-added').text("Added! \u2713");

    setTimeout(function () {
        btn.removeClass('btn-added').text(originalText);
    }, 1000);

    // alert(name + " added to cart!"); // Removed blocking alert in favor of animation
}

function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
}

function loadCartTable() {
    var tableBody = $("#cartTableBody");
    if (!tableBody.length) return;

    tableBody.empty();
    var total = 0;
    cart.forEach(item => {
        var itemTotal = item.price * item.qty;
        total += itemTotal;
        tableBody.append(`
            <tr>
                <td>${item.name}</td>
                <td>$${item.price.toFixed(2)}</td>
                <td>
                    <button class="btn btn-sm btn-secondary" onclick="updateQty(${item.id}, ${item.qty - 1})">-</button>
                    ${item.qty}
                    <button class="btn btn-sm btn-secondary" onclick="updateQty(${item.id}, ${item.qty + 1})">+</button>
                </td>
                <td>$${itemTotal.toFixed(2)}</td>
                <td><button class="btn btn-danger btn-sm" onclick="removeFromCart(${item.id})">Remove</button></td>
            </tr>
        `);
    });
    $("#grandTotal").text(total.toFixed(2));
}

function updateQty(id, newQty) {
    if (newQty < 1) {
        if (confirm("Remove item from cart?")) {
            removeFromCart(id);
        }
        return;
    }
    var item = cart.find(i => i.id === id);
    if (item) {
        item.qty = newQty;
        saveCart();
        loadCartTable();
    }
}

function removeFromCart(id) {
    cart = cart.filter(i => i.id !== id);
    saveCart();
    loadCartTable();
}

function checkout() {
    if (cart.length === 0) {
        alert("Cart is empty!");
        return;
    }

    var customerName = prompt("Enter Customer Name for Order:");
    if (!customerName) return;

    var orderData = {
        customer_name: customerName,
        grand_total: parseFloat($("#grandTotal").text()),
        order_details: cart.map(item => ({
            product_id: item.id,
            quantity: item.qty,
            total_price: item.price * item.qty
        }))
    };

    $.ajax({
        url: orderSaveApiUrl,
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ data: orderData }),
        success: function (response) {
            alert("Order placed successfully! Order ID: " + response.order_id);
            cart = [];
            saveCart();
            window.location.href = "/";
        },
        error: function (err) {
            alert("Error placing order. Please try again.");
            console.error(err);
        }
    });
}

$(document).ready(function () {
    updateCartCount();
    if (window.location.pathname.includes('cart')) {
        loadCartTable();
    }
});
