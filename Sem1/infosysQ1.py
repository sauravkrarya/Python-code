# you are given a weighted Tree T with N nodes.

# it is given that a node N + 1 will be added to T using some same edge (U, N + 1) where U will be chosen randomly. The weight c of this edge will be chosen randomly from the range [1, x]

# Find the expected longest path in T after adding the edge (U, W + 1, c) Since the answer can be very large, return it modulo 10 ^ 9 + 7

# Input Format

# The first line contains an integer, N, denoting the number of nodes in the tree.

# The next line contains an integer, M, denoting the number of rows in edges.

# The next line contains an integer, cols, denoting the number of columns in edges.

# The next line contains an integer, X, denoting the number described in the problem statement.

# Each line i of the M subsequent lines (where 0 <= i < M ) contains cols space separated integers each describing the row edges[i].

# Constraints

# 1 <= N <= 10 ^ 5

# 1 <= M <= 10 ^ 5

# 3 <= cols <= 3

# import sys
# from collections import defaultdict, deque

# MOD = 10**9 + 7

# def bfs_longest_path(tree, start):
#     def bfs(node):
#         visited = [-1] * len(tree)
#         queue = deque([(node, 0)])
#         visited[node] = 0
#         farthest_node, max_distance = node, 0
#         while queue:
#             current, dist = queue.popleft()
#             for neighbor, weight in tree[current]:
#                 if visited[neighbor] == -1:
#                     visited[neighbor] = dist + weight
#                     queue.append((neighbor, dist + weight))
#                     if visited[neighbor] > max_distance:
#                         max_distance = visited[neighbor]
#                         farthest_node = neighbor
#         return farthest_node, max_distance

#     farthest_node, _ = bfs(start)
#     _, longest_path = bfs(farthest_node)
#     return longest_path

# def get_ans(N, M, cols, X, edges):
#     tree = defaultdict(list)
#     for u, v, w in edges:
#         tree[u-1].append((v-1, w))
#         tree[v-1].append((u-1, w))
    
#     total_sum = 0
#     for u in range(N):
#         for c in range(1, X + 1):
#             tree[N] = [(u, c)]
#             tree[u].append((N, c))

#             longest_path = bfs_longest_path(tree, u) + c
#             total_sum += longest_path
#             total_sum %= MOD

#             tree[u].pop()
#             tree[N] = []

#     expected_value = total_sum * pow(N * X, MOD - 2, MOD) % MOD
#     return expected_value

# def main():
#     input = sys.stdin.read
#     data = input().split()
    
#     index = 0
#     N = int(data[index])
#     index += 1
#     M = int(data[index])
#     index += 1
#     cols = int(data[index])
#     index += 1
#     X = int(data[index])
#     index += 1
    
#     edges = []
#     for _ in range(M):
#         edge = list(map(int, data[index:index+cols]))
#         edges.append(edge)
#         index += cols

#     result = get_ans(N, M, cols, X, edges)
#     print(result)

# if __name__ == "__main__":
#     main()




# import sys
# from collections import defaultdict, deque

# MOD = 10**9 + 7

# def bfs(tree, start, N):
#     visited = [-1] * (N + 1)
#     queue = deque([(start, 0)])
#     visited[start] = 0
#     farthest_node, max_distance = start, 0
#     while queue:
#         current, dist = queue.popleft()
#         for neighbor, weight in tree[current]:
#             if visited[neighbor] == -1:
#                 visited[neighbor] = dist + weight
#                 queue.append((neighbor, dist + weight))
#                 if visited[neighbor] > max_distance:
#                     max_distance = visited[neighbor]
#                     farthest_node = neighbor
#     return farthest_node, max_distance

# def find_longest_path(tree, N):
#     # Start BFS from node 0 (or any node) to find the farthest node from it
#     start_node = 0
#     farthest_node, _ = bfs(tree, start_node, N)
#     # Start BFS from the farthest node found to get the longest path
#     _, longest_path = bfs(tree, farthest_node, N)
#     return longest_path

# def get_expected_longest_path(N, M, cols, X, edges):
#     tree = defaultdict(list)
#     for u, v, w in edges:
#         tree[u - 1].append((v - 1, w))
#         tree[v - 1].append((u - 1, w))
    
#     total_longest_path = 0
#     # We consider adding the new node (N) to each of the existing nodes (0 to N-1) with each possible weight (1 to X)
#     for u in range(N):
#         for c in range(1, X + 1):
#             tree[N].append((u, c))
#             tree[u].append((N, c))
#             longest_path = find_longest_path(tree, N) + c
#             total_longest_path += longest_path
#             total_longest_path %= MOD
#             tree[N].pop()
#             tree[u].pop()

#     # The expected value is the average of all possible longest paths
#     total_combinations = N * X
#     expected_value = total_longest_path * pow(total_combinations, MOD - 2, MOD) % MOD
#     return expected_value

# def main():
#     input = sys.stdin.read
#     data = input().split()
    
#     index = 0
#     N = int(data[index])
#     index += 1
#     M = int(data[index])
#     index += 1
#     cols = int(data[index])
#     index += 1
#     X = int(data[index])
#     index += 1
    
#     edges = []
#     for _ in range(M):
#         edge = list(map(int, data[index:index + cols]))
#         edges.append(edge)
#         index += cols

#     result = get_expected_longest_path(N, M, cols, X, edges)
#     print(result)

# if __name__ == "__main__":
#     main()

import sys
from collections import defaultdict, deque

MOD = 10**9 + 7

def bfs(tree, start, N):
    visited = [-1] * (N + 1)
    queue = deque([(start, 0)])
    visited[start] = 0
    farthest_node, max_distance = start, 0
    while queue:
        current, dist = queue.popleft()
        for neighbor, weight in tree[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = dist + weight
                queue.append((neighbor, dist + weight))
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_node = neighbor
    return farthest_node, max_distance

def find_longest_path(tree, N):
    # Start BFS from node 0 (or any node) to find the farthest node from it
    start_node = 0
    farthest_node, _ = bfs(tree, start_node, N)
    # Start BFS from the farthest node found to get the longest path
    _, longest_path = bfs(tree, farthest_node, N)
    return longest_path

def get_expected_longest_path(N, M, cols, X, edges):
    tree = defaultdict(list)
    for u, v, w in edges:
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    
    initial_longest_path = find_longest_path(tree, N)
    
    total_longest_path = 0
    # We consider adding the new node (N) to each of the existing nodes (0 to N-1) with each possible weight (1 to X)
    for u in range(N):
        for c in range(1, X + 1):
            tree[N].append((u, c))
            tree[u].append((N, c))
            longest_path = find_longest_path(tree, N + 1)
            total_longest_path += longest_path
            total_longest_path %= MOD
            tree[N].pop()
            tree[u].pop()

    # The expected value is the average of all possible longest paths
    total_combinations = N * X
    expected_value = (total_longest_path * pow(total_combinations, MOD - 2, MOD)) % MOD
    return expected_value

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    M = int(data[index])
    index += 1
    cols = int(data[index])
    index += 1
    X = int(data[index])
    index += 1
    
    edges = []
    for _ in range(M):
        edge = list(map(int, data[index:index + cols]))
        edges.append(edge)
        index += cols

    result = get_expected_longest_path(N, M, cols, X, edges)
    print(result)

if __name__ == "__main__":
    main()