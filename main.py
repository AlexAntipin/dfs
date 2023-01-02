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
            for i in range(len(matrix[v])):
                if matrix[v][i] == 1 and i not in visited:
                    dfs_help(i, visited)
            self.visited = visited
        dfs_help(v, visited)

        print(visited)

    def bfs(self, v, queue, visited):
        v -= 1
        visited.append(v)
        queue.append(v)

        while queue:
            ver = queue.pop(0)
            for i in range(len(self.matrix[ver])):
                if self.matrix[ver][i] == 1 and i not in visited:
                    visited.append(i)
                    queue.append(i)
        print(visited)


        # def bfs_help(v, visited, queue):








with open('Graph.txt', 'r') as graph:
    matrix = []
    for i in graph.readlines():
        matrix.append(list(map(int,(i[:-1].split()))))


a = Graph(matrix)
a.print_graph()
a.dfs(1,[])
print('Обход в ширину')
a.bfs(3, [], [])

print('Hello world')

