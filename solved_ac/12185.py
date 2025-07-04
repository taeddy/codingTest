# GBus count (Large)
# https://www.acmicpc.net/problem/12185

def solution():
    N = int(input())
    bus_ranges_str = input().split()
    bus_ranges = []
    for i in range(0, 2 * N, 2):
        bus_ranges.append((int(bus_ranges_str[i]), int(bus_ranges_str[i+1])))

    P = int(input())
    query_cities = []
    for _ in range(P):
        query_cities.append(int(input()))

    # Max city number is 5000 based on problem constraints (implicitly)
    # So we need an array up to 5001 (index 0 to 5000)
    city_counts = [0] * 5002 

    for start, end in bus_ranges:
        city_counts[start] += 1
        if end + 1 <= 5001: # Ensure we don't go out of bounds
            city_counts[end + 1] -= 1

    # Calculate prefix sums
    for i in range(1, 5002):
        city_counts[i] += city_counts[i-1]

    results = []
    for city in query_cities:
        results.append(str(city_counts[city]))
    
    return " ".join(results)

T = int(input())
for i in range(1, T + 1):
    result = solution()
    print(f"Case #{i}: {result}")
    if i < T: # Handle the blank line separation for Kickstart
        input()