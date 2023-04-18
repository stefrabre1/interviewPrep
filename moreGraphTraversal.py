# practicing various graph traversal algorithms

## BFS

# input: Graph (V, E) 

# for v in vertices:
    # dist(u) = max
   
# dist(s) = 0
# Q = [s]
# while Q is not None:
    # u = Q.pop
    # for e in edges:
        # if dist(v) = max:   
            # Q.push(v)
            # dist(v) = dist(u) + 1
            
## Dijkstra's
## vertices need to be a class with a neighbors list (which also measure edge weights) and a distance variable

# X = []
# F = [s]

# for v in V:
    # v.dist = max
    
# s.dist = 0

# while F is not None:
    # Pick v (use priority queue, means that we pick the v in F such that v.dist is the smallest value)
    # for u in v.neighbors:
        # if u.dist > v.dist + v.neighbors[u].weight
            # F.push(u)
            # u.dist = v.dist + v.neighbors[u].weight
    # X.push(F.pop)
    
