def sequential_search_loyalty_id(array, find_number):
    """
    Real-life Case: A retail cashier checks if a customer's specific 
    loyalty ID exists in today's transaction log by scanning sequentially.
    """
    pos = "Notfound"
    for i in range(len(array)):
        if array[i] == find_number:
            pos = i
            break
            
    return f"{find_number} Position {pos}"

daily_customer_ids = [20, 30, 40, 50, 60]
print(sequential_search_loyalty_id(daily_customer_ids, 40))