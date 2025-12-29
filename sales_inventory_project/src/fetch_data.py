from db_connection import get_connection

import numpy as np

conn = get_connection()
cursor = conn.cursor()

cursor.execute(""" SELECT p.price,s.quantity from sales s join products p ON s.product_id = p.product_id """)

data = cursor.fetchall()
conn.close()

print(data)

sales_array = np.array(data)