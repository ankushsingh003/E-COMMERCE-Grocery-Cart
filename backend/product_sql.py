import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "sangita143@H"),
        database=os.environ.get("DB_NAME", "gs")
    )

def get_all_products():
    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = "SELECT products.product_id , products.name , products.uom_id , products.price_per_unit , uom.uom_name FROM products inner join uom on products.uom_id=uom.uom_id"
    response = []
    cursor.execute(query)

    for (product_id , name , uom_id , price_per_unit , uom_name) in cursor:
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit,
            "uom_name": uom_name
        })

    cnx.close()
    return response


def insert_new_product(product_name, uom_id, price_per_unit):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = "INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
    cursor.execute(query, (product_name, uom_id, price_per_unit))
    cnx.commit()

    cnx.close()
    return True

def get_uoms():
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM uom"
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({"uom_id": uom_id, "uom_name": uom_name})
    cnx.close()
    return response

def insert_order(order):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    
    # Insert Order
    order_query = "INSERT INTO orders (customer_name, total_price, date_time) VALUES (%s, %s, NOW())"
    cursor.execute(order_query, (order['customer_name'], order['grand_total']))
    order_id = cursor.lastrowid
    
    # Insert Order Details
    detail_query = "INSERT INTO order_details (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
    order_details = []
    for detail in order['order_details']:
        order_details.append((
            order_id,
            int(detail['product_id']),
            float(detail['quantity']),
            float(detail['total_price'])
        ))
    cursor.executemany(detail_query, order_details)
    
    cnx.commit()
    cnx.close()
    return order_id

if __name__ == "__main__":
    print(get_all_products())
    # insert_new_product("bread", 1, 10) 
    # print(get_all_products())


