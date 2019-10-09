import pytest
from ..cube.Cube import Frontier
import time
import os
from cube.Cube import Cube
from copy import deepcopy


def test_force_data_structure():
    test_file = '../resources/test.json'
    try:
        frontier = Frontier()
        x = Cube(test_file)
        x.moveB("l1")
        begin_time = time.time()
        while True:
            y.deepcopy(x)
            frontier.Insert(y)
    except:
        end_time = time.time()
        
    total_time = end_time - begin_time
    print(total_time)
    
def main():
    test_force_data_structure()
    
if __name__ == "__main__":
    main()
    pass
