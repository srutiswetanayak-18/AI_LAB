from collections import deque, defaultdict

def bfs(student_graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print("Exploring node:", current_node)
            visited.add(current_node)
            for neighbor in student_graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return list(visited)

print("---Building Graph---")
student_graph = defaultdict(list)
num_edges = int(input("How many edges (connections) does your graph have? = "))
print("Enter each edge separated by a space (e.g., A B):")
for i in range(num_edges):
    u, v = input(f"Edge {i+1}: ").split()
    student_graph[u].append(v)
    student_graph[v].append(u)

start = input("Enter the starting node for BFS: ")
print(f"\nYour Graph Dictionary: {dict(student_graph)}")
print("Starting BFS Traversal....")
bfs(student_graph, start)
