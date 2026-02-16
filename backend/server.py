from flask import Flask, request, jsonify, render_template
import mysql.connector
from product_sql import get_all_products, insert_new_product, get_uoms, insert_order

app = Flask(__name__, template_folder='../UI/templates', static_folder='../UI/static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/manage-product', methods=['GET'])
def manage_product():
    return render_template('manage_product.html')

@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')

@app.route('/cart', methods=['GET'])
def cart_view():
    return render_template('cart.html')

@app.route('/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product_name = data['name']
    uom_id = data['uom_id']
    price_per_unit = data['price_per_unit']
    insert_new_product(product_name, uom_id, price_per_unit)
    return jsonify({'message': 'Product added successfully'})

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = get_uoms()
    return jsonify(response)

@app.route('/insertOrder', methods=['POST'])
def insert_order_route():
    data = request.get_json()
    order_id = insert_order(data['data'])
    return jsonify({'order_id': order_id})

if __name__ == "__main__":
    app.run(debug=True)
    