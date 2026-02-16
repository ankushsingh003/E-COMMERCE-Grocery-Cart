import mysql.connector

try:
    cnx = mysql.connector.connect(host="localhost", user="root", password="sangita143@H", database="gs")
    cursor = cnx.cursor()
    
    print("Connected to DB")
    
    cursor.execute("SHOW TABLES")
    tables = [x[0] for x in cursor.fetchall()]
    print("Tables:", tables)
    
    if 'orders' in tables:
        cursor.execute("DESCRIBE orders")
        print("\nOrders Schema:")
        for col in cursor.fetchall():
            print(col)
            
    if 'order_details' in tables:
        cursor.execute("DESCRIBE order_details")
        print("\nOrder Details Schema:")
        for col in cursor.fetchall():
            print(col)
            
    cnx.close()
except Exception as e:
    print("Error:", e)
