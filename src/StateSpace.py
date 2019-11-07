import src.Cube as Cube
from copy import deepcopy


class StateSpace:
    @staticmethod
    def successors(cube):
        """Return the successors list of a cube

        Arguments:
            cube -- a cube object

        Returns:
            list -- Formed by a 3-tuples with: the movement, the successor cube and the movement cost
        """
        possible_successors = []
        for movement in cube.valid_movements():
            successor_cube = deepcopy(cube)
            successor_cube.move(movement)
            possible_successors.append([movement, successor_cube, 1])
        return possible_successors


if __name__ == "__main__":
    x = Cube.Cube("resources/cube.json")
    successor = StateSpace.successors(x)
    for element in successor:
        print(element[1].create_md5())
