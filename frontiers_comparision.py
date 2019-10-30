from src.Frontier_SortedList import Frontier_SortedList
import time
import os
import matplotlib.pyplot as plt
from src.Frontier_blist import Frontier_blist
from src.TreeNode import TreeNode
from copy import deepcopy
from src.Cube import Cube
import os
from psutil import virtual_memory


def test_force_sorted_list():
    """This is a stress test that measures the time that SortedList library is over
    """

    begin_time = 0
    frontier = Frontier_SortedList()
    cube = Cube('src/resources/cube.json')
    tree_node = TreeNode('fkldshfñgsdl',cube,3,4,None)
    begin_time = time.time()
    while True:
        tree_node_clone = deepcopy(tree_node)
        frontier.insert(tree_node_clone)
        if(virtual_memory()[2] >= 85):
            break

    end_time = time.time()
    total_time = end_time - begin_time
    return len(frontier) / total_time

def test_force_blist():

    begin_time = 0
    frontier = Frontier_blist()
    cube = Cube('src/resources/cube.json')
    tree_node = TreeNode('fkldshfñgsdl',cube,3,4,None)
    begin_time = time.time()
    while True:
        tree_node_clone = deepcopy(tree_node)
        frontier.insert(tree_node_clone)
        if(virtual_memory()[2] >= 85):
            break

    end_time = time.time()
    total_time = end_time - begin_time
    return len(frontier) / total_time
    

if __name__ == "__main__":
    i=0
    sorted_list=[]
    b_list=[]
    while i<3:
        print("Iteration:", i)
        sorted_list.append(test_force_sorted_list())
        b_list.append(test_force_blist())
        if sorted_list[i] / b_list[i] >= 1 :
            print("The ratio elements per second is higher in sorted list library, exactly: {0:.2f}".format(sorted_list[i] / b_list[i]))
        else:
            print("The ratio elements per second is higher in b_list library, exactly: {0:.2f}".format(sorted_list[i] / b_list[i]))
        i=i+1
    