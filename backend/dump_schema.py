import mysql.connector

try:
    cnx = mysql.connector.connect(host="localhost", user="root", password="sangita143@H", database="gs")
    cursor = cnx.cursor()
    cursor.execute("DESCRIBE orders")
    with open("schema_dump.txt", "w") as f:
        f.write("--- ORDERS TABLE SCHEMA ---\n")
        for col in cursor.fetchall():
            f.write(f"Column: {col[0]}, Type: {col[1]}\n")
            
    cursor.execute("DESCRIBE order_details")
    with open("schema_dump.txt", "a") as f:
        f.write("\n--- ORDER DETAILS SCHEMA ---\n")
        for col in cursor.fetchall():
            f.write(f"Column: {col[0]}, Type: {col[1]}\n")
            
    cnx.close()
    print("Schema dumped to schema_dump.txt")
except Exception as e:
    with open("schema_dump.txt", "w") as f:
        f.write(f"Error: {e}")
    print("Error:", e)
