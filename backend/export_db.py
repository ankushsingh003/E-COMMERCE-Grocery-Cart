import mysql.connector

def export_db():
    config = {
        'user': 'root',
        'password': 'sangita143@H',
        'host': 'localhost',
        'database': 'gs'
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        with open('init_cloud_db.sql', 'w') as f:
            f.write("-- Database Export for Cloud Migration\n\n")
            
            # Get tables
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            
            for table in tables:
                # Get schema
                cursor.execute(f"SHOW CREATE TABLE {table}")
                create_table_sql = cursor.fetchone()[1]
                f.write(f"DROP TABLE IF EXISTS {table};\n")
                f.write(f"{create_table_sql};\n\n")
                
                # Get data
                cursor.execute(f"SELECT * FROM {table}")
                rows = cursor.fetchall()
                
                if rows:
                    f.write(f"INSERT INTO {table} VALUES\n")
                    values_list = []
                    for row in rows:
                        # Format values properly (strings quoted, None as NULL)
                        formatted_row = []
                        for val in row:
                            if val is None:
                                formatted_row.append("NULL")
                            elif isinstance(val, str):
                                formatted_row.append(f"'{val.replace('\'', '\'\'')}'") # Handle quotes
                            elif isinstance(val, (int, float)):
                                formatted_row.append(str(val))
                            else:
                                formatted_row.append(f"'{str(val)}'")
                        values_list.append(f"({', '.join(formatted_row)})")
                    
                    f.write(",\n".join(values_list))
                    f.write(";\n\n")

        print("Successfully exported database to 'init_cloud_db.sql'")
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    export_db()
