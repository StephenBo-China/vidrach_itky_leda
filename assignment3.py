'''
    This file contains the template for Assignment3.  For testing it, I will place it
    in a different directory, call the function <vidrach_itky_leda>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

def Dijkstra(G,v0,INF=999999):
    book = set()
    minv = v0
    dis = dict((k,INF) for k in G.keys())
    dis[v0] = 0
    while len(book)<len(G):
        book.add(minv)
        for w in G[minv]:
            if dis[minv] + G[minv][w] < dis[w]:
                dis[w] = dis[minv] + G[minv][w]
        new =INF
        for v in dis.keys():
            if v in book: continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return dis

def change_to_node(red_i, red_j, blue_i, blue_j):
    return ",".join(str(i) for i in [red_i, red_j, blue_i, blue_j])

def change_to_index(node):
    temp = node.split(",")
    return [int(temp[0]), int(temp[1]), int(temp[2]),int(temp[3])]

def vidrach_itky_leda(input_file_path, output_file_path):
    n = 3
    test_array = [
#         [1, 2, 4, 3],
#         [3, 4, 1, 2],
#         [3, 1, 2, 3],
#         [2, 3, 1, 2]
        #------------------
#         [1,1],
#         [1,1]
        #------------------
#         [1,2,3],
#         [4,5,6],
#         [3,2,1]
        #-------------------
        [1,4,4],
        [1,2,1],
        [4,4,1]
    ]
    red_i, red_j, blue_i, blue_j = 0, 0, n - 1, n - 1
    graph = dict()
    start_node = change_to_node(red_i, red_j, blue_i, blue_j)
    end_node = change_to_node(n-1,n-1,0,0)
    create_graph(graph, start_node, test_array, n - 1)
    if end_node not in graph:
        return -1
    else:
        return Dijkstra(graph,start_node,INF=999)[end_node]

def get_index(node_index):
    return node_index[0],node_index[1],node_index[2],node_index[3]

def create_graph(graph, node, array, n):
    if node in graph:
        return
    node_neighbors = dict()
    node_index = change_to_index(node)
    red_i, red_j, blue_i, blue_j = get_index(node_index)
    red_step = array[blue_i][blue_j]
    blue_step = array[red_i][red_j]
    # Red go top
    index = red_i - red_step
    if index != red_i and index >= 0:
        next_node = change_to_node(index, red_j, blue_i, blue_j)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)
    # Red go bottom
    index = red_i + red_step
    if index != red_i and index <= n:
        next_node = change_to_node(index, red_j, blue_i, blue_j)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)
    # Red go left
    index = red_j - red_step
    if index != red_j and index >= 0:
        next_node = change_to_node(red_i, index, blue_i, blue_j)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)
    # Red go right
    index = red_j + red_step
    if index != red_j and index <= n:
        next_node = change_to_node(red_i, index, blue_i, blue_j)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)
    # Blue go top
    index = blue_i - blue_step
    if index != blue_i and index >= 0:
        next_node = change_to_node(red_i, red_j, index, blue_j)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)
    # Blue go bottom
    index = blue_i + blue_step
    if index != blue_i and index <= n:
        next_node = change_to_node(red_i, red_j, index, blue_j)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)
    # Blue go left
    index = blue_j - blue_step
    if index != blue_j and index >= 0:
        next_node = change_to_node(red_i, red_j, blue_i, index)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)
    # Blue go right
    index = blue_j + blue_step
    if index != blue_j and index <= n:
        next_node = change_to_node(red_i, red_j, blue_i, index)
        node_neighbors[next_node] = 1
        graph[node] = node_neighbors
        create_graph(graph, next_node, array, n)

print(vidrach_itky_leda(1, 2))




