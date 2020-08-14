"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        edges = self.vertices[v1]
        edges.add(v2)
            
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        
        marked = set()
        
        while q.size() > 0:
            visited = q.dequeue()
            
            if visited not in marked:
                print(visited)
                marked.add(visited)
                
                
                neighbours = self.get_neighbors(visited)
                for neighbour in neighbours:
                    q.enqueue(neighbour)
                    
        return marked

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        
        marked = set()
        
        while s.size() > 0:
            visited = s.pop()
            
            if visited not in marked:
                print(visited)
                marked.add(visited)
                
                neighbours = self.get_neighbors(visited)
                for neighbour in neighbours:
                    s.push(neighbour)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        marked = set()
        
        def dft_inner(visited):
            if visited in marked:
                return
            
            marked.add(visited)
            print(visited)
            
            for vertex in self.vertices[visited]:
                dft_inner(vertex)
        
        dft_inner(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        
        paths = set()
        
        while q.size() > 0:
            current = q.dequeue()
            vertex = current[-1]

            if vertex not in paths:  
                if vertex == destination_vertex:
                    return current   
                     
                paths.add(vertex)
                
                for neighbor in self.vertices[vertex]:
                    path = [*current]
                    path.append(neighbor)
                    q.enqueue(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        
        paths = set()
        
        while s.size() > 0:
            current = s.pop()
            last_vertex = current[-1]
            
            if last_vertex not in paths:
                if last_vertex == destination_vertex:
                    return current
                
                paths.add(last_vertex)
               
                for neighbor in self.vertices[last_vertex]:
                    path = [*current]
                    path.append(neighbor)
                    s.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        marked = set()
        paths = []
         
        def dfs_inner(starting_vertex, destination_vertex, paths):
            if starting_vertex in marked:
                return paths
            
            elif starting_vertex == destination_vertex:
                paths.append(starting_vertex)
                return paths
            
            marked.add(starting_vertex)
            for neighbour in self.vertices[starting_vertex]:
                if destination_vertex in dfs_inner(neighbour, destination_vertex, paths):
                    paths.append(starting_vertex)
                    return paths
                
            return paths
        
        path = dfs_inner(starting_vertex, destination_vertex, paths)
        
        return path[::-1]
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
