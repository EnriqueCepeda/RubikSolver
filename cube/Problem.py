from StateSpace import StateSpace
from Cube import Cube
from numpy import array, nditer

class Problem:

    def __init__(self, state_space, initial_state):
        self.stateSpace = state_space
        self.initialState = initial_state

    def isGoal(self, state):
        """This function checks if a certain state of the cube is solved.
        
        Returns:
            True/False -- Boolean that represents if each of the faces is diferent from each one
        """
        number_list = []

        if not self.__check_correctness_face(state.back, number_list):
            return False
        if not self.__check_correctness_face(state.down, number_list):
            return False
        if not self.__check_correctness_face(state.front, number_list):
            return False
        if not self.__check_correctness_face(state.left, number_list):
            return False
        if not self.__check_correctness_face(state.right, number_list):
            return False
        if not self.__check_correctness_face(state.up, number_list):
            return False

        return number_list.sort() == [0,1,2,3,4,5]


    def __check_correctness_face(self, face, number_list):
        """This function checks the correctness of a certain face of the state(cube)
        
        Returns:
            True/False -- Boolean that represents if all the numbers of the face are equal to the first one
        """
        first_number_face = face[0]
        for number in nditer(face):
            if first_number_face != number:
                return False

        number_list.add(first_number_face)
        return True
