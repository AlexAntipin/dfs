import re





class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.visited = []

    def print_graph(self):
        print(self.matrix)

    def dfs(self, v, visited):
        v -= 1
        def dfs_help(v, visited):
            visited.append(v)
            print(visited)
            for i in range(len(matrix[v])):
                if matrix[v][i] == 1 and i not in visited:
                    dfs_help(i, visited)
            self.visited = visited
        dfs_help(v, visited)


with open('Graph.txt', 'r') as graph:
    matrix = []
    for i in graph.readlines():
        matrix.append(list(map(int,(i[:-1].split()))))

    print(matrix)

a = Graph(matrix)
a.print_graph()
a.dfs(1,[])

print('Hello world')

