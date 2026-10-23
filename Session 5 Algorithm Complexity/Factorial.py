def calculate_factorial_orders(n):
    """
    Real-life Case: A manufacturing plant calculates how many different 
    sequential production schedules (n!) are possible for a batch of n custom orders.
    """
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

num_orders = 5
print(f"Total possible scheduling sequences for {num_orders} orders: {calculate_factorial_orders(num_orders)}")