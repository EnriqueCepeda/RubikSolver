import json
import hashlib
from matplotlib import pyplot as plt
from matplotlib import patches
from numpy import array, rot90, nditer, copy, flip
from math import sqrt
from os import path
from sys import exit
import codecs
from copy import deepcopy
from math import log


class Cube:
    def __init__(self, json_file=None, *args, **kwargs):
        """This function is the constructor of the class

        Arguments:
            json_file -- Is the path of the json file where the cube configuration is stored (default: {None})
            kwargs -- If the method is called with a positional argument formed by 6 elements then the json file opening is omitted, and the cube is formed by those six elements

        """
        if len(args) != 1:
            try:
                with open(json_file, "r") as f:
                    cube_configuration = json.load(f)
            except FileNotFoundError as e:
                print(e)
                exit()

            else:
                self.left = array(cube_configuration["LEFT"], dtype="int8")
                self.right = array(cube_configuration["RIGHT"], dtype="int8")
                self.up = array(cube_configuration["UP"], dtype="int8")
                self.down = array(cube_configuration["DOWN"], dtype="int8")
                self.back = array(cube_configuration["BACK"], dtype="int8")
                self.front = array(cube_configuration["FRONT"], dtype="int8")
                self.n = int(sqrt(self.left.size))
        else:
            self.left = args[0][4]
            self.right = args[0][5]
            self.up = args[0][0]
            self.down = args[0][1]
            self.back = args[0][3]
            self.front = args[0][2]
            self.n = int(sqrt(self.left.size))

    def __str__(self):
        """This function does the representation of the cube

        Returns:
            string -- Returns the different faces of the cube
        """
        return (
            str(self.back)
            + " BACK \n"
            + str(self.down)
            + " DOWN \n"
            + str(self.front)
            + " FRONT \n"
            + str(self.left)
            + " LEFT \n"
            + str(self.right)
            + " RIGHT \n"
            + str(self.up)
            + " UP \n"
        )

    def clone(self):
        """Clones a certain cube in the space memory

        Returns:
            cube Object
        """

        return deepcopy(self)

    def create_md5(self):
        """Does an md5 string with the cube configuration

        Returns:
            string -- returns the identifier of the cube state which depends of the colors combination
        """
        string = ""
        for number in nditer(self.back):
            string += str(number)
        for number in nditer(self.down):
            string += str(number)
        for number in nditer(self.front):
            string += str(number)
        for number in nditer(self.left):
            string += str(number)
        for number in nditer(self.right):
            string += str(number)
        for number in nditer(self.up):
            string += str(number)
        hash = hashlib.md5(string.encode())
        return hash.hexdigest()

    def to_json(self, *args):
        """Generates a json file with cube configuration

        Arguments:
            args {
                args[0] - string - This string tells the method where to store the json file

            } 
        """
        cube_json = {
            "BACK": self.back.tolist(),
            "DOWN": self.down.tolist(),
            "FRONT": self.front.tolist(),
            "LEFT": self.left.tolist(),
            "RIGHT": self.right.tolist(),
            "UP": self.up.tolist(),
        }

        with open(args[0], "w") as f:
            json.dump(cube_json, f)

    def save_img(self, name):
        """This function saves the configuration of the cube  in an .svg image

        Parameters:
            name - Type: String - Desscription: Is the name of the path where the svg_file is
        """
        self.plot_cube(name).savefig("resources/" + name, format="svg")

    def plot_cube(self, svg_path):
        """This function plots the matrix of the cube hiding the axes of each side of the cube

        Parameters: 
            svg_path - Type: String - Description: Is the path where the svg_file is stored
        """
        plot, axes = plt.subplots(3, 4)

        self.plot_face(axes[0, 1], self.back)
        axes[0, 1].set_title("BACK")
        self.plot_face(axes[1, 1], self.down)
        axes[1, 1].set_title("DOWN")
        self.plot_face(axes[2, 1], self.front)
        axes[2, 1].set_title("FRONT")
        self.plot_face(axes[1, 0], self.left)
        axes[1, 0].set_title("LEFT")
        self.plot_face(axes[1, 2], self.right)
        axes[1, 2].set_title("RIGHT")
        self.plot_face(axes[1, 3], self.up)
        axes[1, 3].set_title("UP")

        for axis in axes.flat:
            axis.axis(False)

        plot.suptitle(svg_path)
        plt.autoscale()
        plt.pause(1)

        return plot

    def plot_face(self, axes, face):
        """This function plots the matrix of a certain face of the cube 

        Parameters:
            axes - Type: axes_object - Description: Is the axes object which is added to the plot which is converted in the cube image
            face - Type: matrix - Description: Is the cube side which is going to be plotted

            """
        colorlist = ["red", "blue", "yellow", "green", "orange", "white"]

        square_side_length = 1 / self.n

        coordinate_y = 1 - (square_side_length)
        coordinate_x = 0
        for row in face:
            for number in row:
                square = patches.Rectangle(
                    (coordinate_x, coordinate_y),
                    square_side_length,
                    square_side_length,
                    linewidth=2,
                    edgecolor="black",
                    facecolor=colorlist[number],
                )
                axes.add_patch(square)
                coordinate_x += square_side_length
            coordinate_x -= 1
            coordinate_y -= square_side_length

    def valid_movements(self):
        """
        This method returns all the valid movements from a cube of n dimensions
        """
        return [
            letter + str(number)
            for letter in ["B", "b", "D", "d", "L", "l"]
            for number in range(0, self.n)
        ]

    def __moveL(self, *args):
        """
        This function does the L and l axis moves
        """

        axis = args[0]
        axis_depth = int(args[1])

        if axis.islower():
            aux_down = self.down[:, axis_depth].copy()
            self.down[:, axis_depth] = self.back[:, axis_depth]
            self.back[:, axis_depth] = flip(
                self.up[:, self.n - 1 - axis_depth])
            self.up[:, self.n - 1 -
                    axis_depth] = flip(self.front[:, axis_depth])
            self.front[:, axis_depth] = aux_down

            if axis_depth == 0:
                self.left = rot90(self.left, 1)
                self.left = (
                    self.left.copy()
                )  # Necessary to update the reference of the face
            elif axis_depth == self.n - 1:
                self.right = rot90(self.right, 1)
                self.right = (
                    self.right.copy()
                )  # Necessary to update the reference of the face
        else:
            aux_up = self.up[:, self.n - 1 - axis_depth].copy()
            self.up[:, self.n - 1 -
                    axis_depth] = flip(self.back[:, axis_depth])
            self.back[:, axis_depth] = self.down[:, axis_depth]
            self.down[:, axis_depth] = self.front[:, axis_depth]
            self.front[:, axis_depth] = flip(aux_up)

            if axis_depth == 0:
                self.left = rot90(self.left, 3)
                self.left = (
                    self.left.copy()
                )  # Necessary to update the reference of the face
            elif axis_depth == self.n - 1:
                self.right = rot90(self.right, 3)
                self.right = (
                    self.right.copy()
                )  # Necessary to update the reference of the face

    def __moveD(self, *args):
        """
        This function does the D and d axis moves
        """
        axis = args[0]
        axis_depth = int(args[1])

        if axis.islower():

            aux_back = flip(self.back[self.n - 1 - axis_depth, :].copy())

            self.back[self.n - 1 - axis_depth,
                      :] = self.right[:, axis_depth].copy()
            self.right[:, axis_depth] = flip(self.front[axis_depth, :].copy())
            self.front[axis_depth, :] = self.left[:,
                                                  self.n - 1 - axis_depth].copy()
            self.left[:, self.n - 1 - axis_depth] = aux_back

            if axis_depth == 0:
                self.down = rot90(self.down, 1)
                self.down = (
                    self.down.copy()
                )  # Necessary to update the reference of the face
            elif axis_depth == self.n - 1:
                self.up = rot90(self.up, 1)
                self.up = (
                    self.up.copy()
                )  # Necessary to update the reference of the face
        else:

            aux_back = self.back[self.n - 1 - axis_depth, :].copy()

            self.back[self.n - 1 - axis_depth, :] = flip(
                self.left[:, self.n - 1 - axis_depth].copy()
            )
            self.left[:, self.n - 1 -
                      axis_depth] = self.front[axis_depth, :].copy()
            self.front[axis_depth, :] = flip(self.right[:, axis_depth].copy())
            self.right[:, axis_depth] = aux_back

            if axis_depth == 0:
                self.down = rot90(self.down, 3)
                self.down = (
                    self.down.copy()
                )  # Necessary to update the reference of the face
            elif axis_depth == self.n - 1:
                self.up = rot90(self.up, 3)
                self.up = (
                    self.up.copy()
                )  # Necessary to update the reference of the face

    def __moveB(self, *args):
        """
        This function does the B and b axis moves
        """
        axis = args[0]
        axis_depth = int(args[1])

        if axis.islower():

            aux_left = self.left[axis_depth, :].copy()

            self.left[axis_depth, :] = self.down[axis_depth, :]
            self.down[axis_depth, :] = self.right[axis_depth, :]
            self.right[axis_depth, :] = self.up[axis_depth, :]
            self.up[axis_depth, :] = aux_left

            if axis_depth == 0:
                self.back = rot90(self.back, 1)
                self.back = (
                    self.back.copy()
                )  # Necessary to update the reference of the face
            elif axis_depth == self.n - 1:
                self.front = rot90(self.front, 1)
                self.front = (
                    self.front.copy()
                )  # Necessary to update the reference of the face

        else:

            aux_left = self.left[axis_depth, :].copy()

            self.left[axis_depth, :] = self.up[axis_depth, :]
            self.up[axis_depth, :] = self.right[axis_depth, :]
            self.right[axis_depth, :] = self.down[axis_depth, :]
            self.down[axis_depth, :] = aux_left

            if axis_depth == 0:
                self.back = rot90(self.back, 3)
                self.back = (
                    self.back.copy()
                )  # Necessary to update the reference of the face
            elif axis_depth == self.n - 1:
                self.front = rot90(self.front, 3)
                self.front = (
                    self.front.copy()
                )  # Necessary to update the reference of the face

    def move(self, movement):

        axis = movement[:1]
        axis_depth = int(movement[1:])

        if axis_depth < self.n:

            if axis.lower() == "l":
                self.__moveL(axis, axis_depth)
            elif axis.lower() == "d":
                self.__moveD(axis, axis_depth)
            else:
                self.__moveB(axis, axis_depth)
        else:
            print("Introduce a valid movement")

    def entropy(self):
        entropy = 0
        counter = []
        faces = [self.left, self.right, self.up,
                 self.down, self.back, self.front]

        for face in faces:
            face_entropy = 0
            counter.clear()
            for number in range(6):
                counter.append(list(face.flatten()).count(number))
                if counter[number] > 0:
                    face_entropy = face_entropy + counter[number] / face.size * log(
                        counter[number] / (face.size), 6
                    )
            entropy += abs(face_entropy)

        return entropy


if __name__ == "__main__":
    x = Cube("resources/heuristic_example.json")
    print(x.entropy())
    x.plot_cube("heuristic_example")
