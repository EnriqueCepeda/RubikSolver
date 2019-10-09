from Cube import Cube
from copy import deepcopy

class StateSpace:

    @staticmethod
    def successors(cube):
        possible_successors=[]
        for movement in cube.valid_movements():
            successor_cube = deepcopy(cube)
            successor_cube.move(movement)
            possible_successors.append([movement,successor_cube,1])
        return possible_successors

    

x = Cube('../resources/cube.json')
successor = StateSpace.successors(x)
for element in successor:
    print(element[1].create_md5())

