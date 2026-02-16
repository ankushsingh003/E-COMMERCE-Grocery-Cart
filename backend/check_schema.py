import mysql.connector

try:
    cnx = mysql.connector.connect(host="localhost", user="root", password="sangita143@H", database="gs")
    cursor = cnx.cursor()
    cursor.execute("DESCRIBE orders")
    print("--- ORDERS TABLE SCHEMA ---")
    for col in cursor.fetchall():
        print(f"Column: {col[0]}, Type: {col[1]}")
    cnx.close()
except Exception as e:
    print("Error:", e)
