from fetch_data import sales_array
from analytics import total_revenue,max_sale,average_order_value

print("Total Revenue:",total_revenue(sales_array))
print("Average order value:",average_order_value(sales_array))
print("Highest sale:",max_sale(sales_array))