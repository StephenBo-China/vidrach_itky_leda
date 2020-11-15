'''
    This file contains the template for Assignment3.  For testing it, I will place it
    in a different directory, call the function <vidrach_itky_leda>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

class Node:
    def __init__(self, red_i, red_j, blue_i, blue_j):
        self.red_i = red_i
        self.red_j = red_j
        self.blue_i = blue_i
        self.blue_j = blue_j
        self.nexts = []
        self.edges = []

class Edge:
    def __init__(self, weight, fro, to):
        self.weight = weight
        self.fro = fro
        self.to = to

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

def vidrach_itky_leda(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''
    n = 3
    test_array = [
        [1,2,4,3],
        [3,4,1,2],
        [3,1,2,3],
        [2,3,1,2]
    ]
    red_i, red_j, blue_i, blue_j =0, 0, n, n
    graph = Graph()
    create_graph(graph, red_i, red_j, blue_i, blue_j, n, test_array)

def get_legal_index(i, n):
    if i < 0:
        return 0
    if i > n:
        return n

def create_graph(graph, red_i, red_j, blue_i, blue_j, n, array):
    node = Node(red_i, red_j, blue_i, blue_j)
    red_step = array[blue_i][blue_j]
    blue_step = array[red_i][red_j]
    # Go Top
    index = i - red_step
    if i - red_step >= 0 and



# vidrach_itky_leda('input0.in', 'input0.out')
