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





class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insertNode(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insertNode(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insertNode(value)
        else:
            self.value = value

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()



root = Node(10)
root.insertNode(6)
root.insertNode(7)
root.insertNode(14)
root.insertNode(5)
root.insertNode(18)

root.PrintTree()
with open('Graph.txt', 'r') as graph:
    matrix = []
    for i in graph.readlines():
        matrix.append(list(map(int,(i[:-1].split()))))


# a = Graph(matrix)
# a.print_graph()
# a.dfs(1,[])
# print('Обход в ширину')
# a.bfs(3, [], [])
#
# print('Hello world')




