from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("INSERT INTO products(product_name,price,stock) values (%s,%s,%s)",("Laptop",55000,50))

cursor.execute("INSERT INTO sales(product_id,quantity,sale_date) values (%s,%s,%s)",(1,2,"2025-12-29"))

conn.commit()
conn.close()


