import pytest
from cube.Frontier import Frontier
import time
from cube.Cube import Cube
from copy import deepcopy

test_file = '../resources/test.json'

def test_force_data_structure():
    
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
    

