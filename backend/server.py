from flask import Flask, request, jsonify, render_template, session, redirect, url_for
import mysql.connector
from product_sql import get_all_products, insert_new_product, get_uoms, insert_order

import os

app = Flask(__name__, template_folder='../UI/templates', static_folder='../UI/static')
app.secret_key = os.environ.get('SECRET_KEY', 'super_secret_key')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'admin@gmail.com' and password == 'admin':
            session['user'] = email
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
    