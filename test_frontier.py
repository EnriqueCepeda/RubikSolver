from src.Frontier_SortedList import Frontier_SortedList
import time
import os
from src.Cube import Cube


def test_force_data_structure():
    test_file = 'src/resources/test.json'
    begin_time = 0
    
    try:
        frontier = Frontier_SortedList()
        x = Cube(test_file)
        x.move("l2")
        begin_time = time.time()
       
        while True:
            y=x.clone()
            frontier.Insert(y)
    except:
        end_time = time.time()
 
    total_time = end_time - begin_time
    print(total_time)
    

if __name__ == "__main__":
    test_force_data_structure()