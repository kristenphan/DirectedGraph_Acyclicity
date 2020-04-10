#Uses python3

import sys

# this function takes in a vertex 'v', adjacent list representation of a directed graph called 'adj',
# and a list called 'visited' to keep track of whether a vertex has been previously visited
# the function's objective is to explore all reachable vertices (a complete path) from vertex v
# and check if there's a cycle on the graph. a cycle can be present in any path on the graph
# if yes, return True
# when exploring a path, the function marks the nodes it has visited so that if it runs into these nodes again, it can detect a cycle on this path
# after finish exploring a complete path on the graph, the function will reset all nodes to be not-visited,
# allowing these nodes to be revisited on another path
def explore(v, adj, visited):
    visited[v] = True
    for adj_node in adj[v]:
        if visited[adj_node]:
            visited[v] = False
            return True
        found = explore(adj_node, adj, visited)
        if found: # check the return value of the recursive call above, if a cycle is found, exit the recursion loop
            return True
    visited[v] = False


# this function takes in an adjacent list representation of a directed graph (adj)
# and checks if there's any cycles in the graph
# if yes, return 1. otherwise, return 0
def acyclic(adj):
    n = len(adj)
    visited = [False for _ in range(n)]
    for v in range(n):
        found = explore(v, adj, visited)
        if found: # a cycle is found in the graph
            return 1
    return 0

# this program reads the input, build a directed graph from the input,
# and checks if the graph contains cycle(s)
# if yes, return 1. otherwise, return 0
# EXAMPLE:
# input:
# 5 7
# 1 2
# 2 3
# 1 3
# 3 4
# 1 4
# 2 5
# 3 5
# output: 0
# graph is visualized as below: 1-based index
#   4 <---- 3 ----> 5
#    ^     ^ ^     ^
#     \   /   \   /
#      1 -----> 2
# graph is visualized as below: 1-based index
#   3 <---- 2 ----> 4
#    ^     ^ ^     ^
#     \   /   \   /
#       0 ----> 1
# adj        = [[1, 2, 3], [2, 4], [3, 4], [], []]
# vertex idx =      0         1       2     3   4
# as depicted in the above graph, there is no cycle
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #adj = [[1, 2, 3], [2, 4], [3, 4], [], []]
    print(acyclic(adj))
