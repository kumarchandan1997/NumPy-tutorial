import numpy as np

def total_revenue(sales_array):
    revenue = sales_array[:,0] * sales_array[:,1]

    return np.sum(revenue)

def average_order_value(sales_array):
    revenue = sales_array[:,0] * sales_array[:,1]
    return np.mean(revenue)

def max_sale(sales_array):
    revenue = sales_array[:,0] * sales_array[:,1]
    return np.max(revenue)