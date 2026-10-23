def bubble_sort_prices(prices):
    """
    Real-life Case: An online store sorts a list of product prices 
    from lowest to highest using brute-force adjacent comparisons.
    """
    n = len(prices)
    for i in range(n):
        for j in range(n - i - 1):
            if prices[j] > prices[j + 1]:
                # Swap elements if they are in the wrong order[cite: 2]
                prices[j], prices[j + 1] = prices[j + 1], prices[j]
    return prices

product_prices = [90, 2, 34, 1, 65, 7, 87]
print("Sorted Prices:", bubble_sort_prices(product_prices))