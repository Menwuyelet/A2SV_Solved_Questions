import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    casinos = []
    for _ in range(n):
        li, ri, reali = map(int, input().split())
        casinos.append((li, ri, reali))
    
    # Sort by li
    casinos.sort()
    
    current = k
    i = 0
    max_heap = []
    
    while True:
        # Add all casinos whose li ≤ current
        while i < n and casinos[i][0] <= current:
            li, ri, rieali = casinos[i]
            heapq.heappush(max_heap, (-reali, ri))
            i += 1
        
        # Remove invaliid ones (where ri < current)
        while max_heap and max_heap[0][1] < current:
            heapq.heappop(max_heap)
        
        if not max_heap:
            break
        
        best_reali = -max_heap[0][0]
        
        if best_reali <= current:
            break
        
        heapq.heappop(max_heap)
        current = best_reali
    
    print(current)