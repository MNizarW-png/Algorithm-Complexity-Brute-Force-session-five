def find_biggest(array):
    """
    Real-life Case: A meteorological station scans daily temperature readings 
    to find the highest temperature of the week.
    """
    max_val = array[0]
    for i in range(1, len(array)):
        if array[i] > max_val:
            max_val = array[i]
            
    return max_val

weekly_temps = [10, 30, 100, 45, 76, 23, 99]
print("Highest Temperature:", find_biggest(weekly_temps))