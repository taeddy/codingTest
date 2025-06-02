N, K, P = map(int, input().split())
breads = list(map(int, input().split()))

# Time Complexity of slicing list = O(k), k = j-i
sellable = 0
for i in range(N):
    start_idx, end_idx = i*K, (i+1)*K
    non_cream_count = 0
    for idx in range(start_idx, end_idx):
        if breads[idx] == 0:
            non_cream_count += 1
    if non_cream_count < P:
        sellable += 1
print(sellable)