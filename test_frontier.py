from src.Frontier_SortedList import Frontier_SortedList
import time
import os
from src.Frontier_SortedSet import Frontier_SortedSet
from src.TreeNode import TreeNode


def test_force_sorted_list():
    """This is a stress test that measures the time that SortedList library is over
    """

    begin_time = 0
    
    try:
        frontier = Frontier_SortedList()
        tree_node = TreeNode(1,2,3,4)
        begin_time = time.time()
       
        while True:
    
            tree_node_clone = tree_node.clone()
            frontier.insert(tree_node_clone)
    except:
        
        end_time = time.time()
 
    total_time = end_time - begin_time
    print("{0:.20f}".format(total_time))

def test_force_sorted_set():

    begin_time = 0
    
    try:
        frontier = Frontier_SortedSet()
        tree_node = TreeNode(1,2,3,4)
        begin_time = time.time()
       
        while True:

            tree_node_clone = tree_node.clone()
            frontier.insert(tree_node_clone)
    except:
        end_time = time.time()
 
    total_time = end_time - begin_time
    print("{0:.20f}".format(total_time))
    

if __name__ == "__main__":
    test_force_sorted_list()
    test_force_sorted_set()