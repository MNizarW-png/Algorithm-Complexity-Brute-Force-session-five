import itertools

print("Note:")
print("A: Warehouse")
print("B: Jakarta")
print("C: Bandung")
print("D: Surabaya")
print("E: Sukabumi")

def solve_tsp_5_nodes():
    """
    Real-life Case: A central delivery warehouse (Node A) needs to visit 
    4 local store branches (B, C, D, E) and return to the warehouse, 
    evaluating all (5-1)! = 24 possible routes to find the shortest distance.
    """
    start_city = 'A'
    other_cities = ['B', 'C', 'D', 'E']
    
    # Distance matrix (weights between all cities)
    distances = {
        ('A', 'B'): 2, ('B', 'A'): 2,
        ('A', 'C'): 9, ('C', 'A'): 9,
        ('A', 'D'): 3, ('D', 'A'): 3,
        ('A', 'E'): 7, ('E', 'A'): 7,
        ('B', 'C'): 4, ('C', 'B'): 4,
        ('B', 'D'): 1, ('D', 'B'): 1,
        ('B', 'E'): 5, ('E', 'B'): 5,
        ('C', 'D'): 6, ('D', 'C'): 6,
        ('C', 'E'): 3, ('E', 'C'): 3,
        ('D', 'E'): 8, ('E', 'D'): 8,
    }
    
    min_weight = float('inf')
    best_routes = []
    
    print(f"Evaluating all (5 - 1)! = 4! = 24 possible routes:")
    
    # Brute force permutation of n-1 vertices
    for perm in itertools.permutations(other_cities):
        route = [start_city] + list(perm) + [start_city]
        weight = 0
        
        for i in range(len(route) - 1):
            weight += distances[(route[i], route[i+1])]
            
        print(f"Route: {' -> '.join(route)}  |  Total Distance: {weight}")
        
        if weight < min_weight:
            min_weight = weight
            best_routes = [route]
        elif weight == min_weight:
            best_routes.append(route)
            
    print(f"\nShortest Route(s) Found with Minimum Weight ({min_weight}):")
    for r in best_routes:
        print(f"  {' -> '.join(r)}")

solve_tsp_5_nodes()