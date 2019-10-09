from src.Frontier import Frontier
import time
import os
import src.Cube


def test_force_data_structure():
    test_file = 'src/resources/test.json'
    begin_time = 0
    try:
        frontier = Frontier()
        x = Cube(test_file)
        print(x)
        print('hemos llegado aqui')
        x.move('l1')
        print('hemos hecho el move')
        begin_time = time.time()
        print(begin_time)
        print('uwu before')
        while True:
            print('uwu')
            y=x.clone()
            frontier.Insert(y)
    except:
        end_time = time.time()
        print('hola')
        
    total_time = end_time - begin_time
    print(total_time)
    

if __name__ == "__main__":
    test_force_data_structure()