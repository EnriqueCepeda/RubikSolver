import json
import hashlib
from numpy import array, rot90, nditer, copy, flip
from math import sqrt
from os import path
from sys import exit
 
class Cube:

    def __init__(self,json_file):

        try:
            with open(path.join(json_file), 'r') as f:
                cube_configuration = json.load(f)
        except FileNotFoundError as e:
            print(e)
            exit()

        else:
            self.left = array(cube_configuration['LEFT'],dtype='int8')
            self.right= array(cube_configuration['RIGHT'],dtype='int8')
            self.up= array(cube_configuration['UP'],dtype='int8')
            self.down= array(cube_configuration['DOWN'],dtype='int8')
            self.back= array(cube_configuration['BACK'],dtype='int8')
            self.front= array(cube_configuration['FRONT'],dtype='int8')
            self.n = int(sqrt(self.left.size))
    
    def __str__(self):
        return str(self.up) + ' UP \n' + str(self.down) + ' DOWN \n' + str(self.left) + ' LEFT \n' + str(self.right) + ' RIGHT \n' + str(self.front) + ' FRONT \n' + str(self.back) + ' BACK \n' 

    def create_md5(self):
        """Does an md5 string with the cube configuration
        
        Returns:
            string -- returns the identifier of the cube state which depends of the colors combination
        """
        string=''
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

    
    def moveL(self,*args):
        """
        This function does the L and l axis moves
        """

        axis = args[0]
        axis_depth = args[1]

        if axis.islower():
            aux_front = self.front[:,axis_depth].copy()
            aux_down = self.down[:,axis_depth].copy()
            aux_back = self.back[:,axis_depth].copy()

            self.down[:,axis_depth] = aux_back
            self.back[:,axis_depth] = self.up[:,self.n - 1 - axis_depth]
            self.up[:,self.n - 1 - axis_depth] = flip(aux_front)
            self.front[:,axis_depth] = aux_down

            self.left = rot90(self.left,1)
        else:
            
            aux_up = self.up[:,self.n - 1 - axis_depth].copy()
            aux_down = self.down[:,axis_depth].copy()
            aux_back = self.back[:,axis_depth].copy()

            self.down[:,axis_depth] = self.front[:,axis_depth] 
            self.back[:,axis_depth] = aux_down
            self.up[:,self.n - 1 - axis_depth] = aux_back
            self.front[:,axis_depth] = aux_up
            self.left = rot90(self.left,3)


    def moveD(self,*args):
        """
        This function does the D and d axis moves
        """
        axis = args[0]
        axis_depth = args[1]
        if axis.islower():
            
            aux_back = self.back[self.n - 1 - axis_depth,:].copy()
            aux_right = self.right[:,axis_depth].copy()
            aux_front = self.front[axis_depth,:].copy()
            aux_left = self.left[:,self.n - 1 - axis_depth].copy()
                      
            self.back[self.n - 1 - axis_depth,:] =aux_right
            self.right[:,axis_depth] = aux_front
            self.front[axis_depth,:] = aux_left
            self.left[:,self.n - 1- axis_depth] = aux_back

            if axis_depth == 0:
                self.down = rot90(self.down,1)
            elif axis_depth == self.n-1:
                self.up = rot90(self.up,1)
        else:

            aux_back = flip(self.back[self.n - 1 - axis_depth,:].copy())
            aux_right = flip(self.right[:,axis_depth].copy())
            aux_front = flip(self.front[axis_depth,:].copy())
            aux_left = flip(self.left[:,self.n - 1 -axis_depth].copy())


            self.back[self.n - 1 - axis_depth,:] = aux_left 
            self.right[:,axis_depth] = aux_back
            self.front[axis_depth] = aux_right
            self.left[:,self.n - 1- axis_depth] = aux_front

            if axis_depth == 0:
                self.down = rot90(self.down,3)
            elif axis_depth == self.n-1:
                self.up = rot90(self.up,3)
    
    def moveB(self,*args):
        """
        This function does the B and b axis moves
        """
        axis = args[0]
        axis_depth = args[1]

        if axis.islower():  

            aux_left = self.left[axis_depth,:].copy()

            self.left[axis_depth,:] = self.down[axis_depth,:]
            self.down[axis_depth,:] = self.right[axis_depth,:]
            self.right[axis_depth,:] = self.up[axis_depth,:]
            self.up[axis_depth,:] = aux_left

            if axis_depth == 0:
                self.back = rot90(self.back,1)
            elif axis_depth == self.n-1:
                self.front = rot90(self.front,1)

        else:  
            
            aux_left = self.left[axis_depth,:].copy()

            self.left[axis_depth,:] = self.up[axis_depth,:] 
            self.up[axis_depth,:] = self.right[axis_depth,:]
            self.right[axis_depth,:] = self.down[axis_depth,:]
            self.down[axis_depth,:] = aux_left

            if axis_depth == 0:
                self.back = rot90(self.back,3)
            elif axis_depth == self.n-1:
                self.front = rot90(self.front,3)


    def move(self, movement):

        axis = movement[:1]
        axis_depth = int(movement[1:])

        if axis_depth < self.n:

            if axis.lower() == 'l':
                self.moveL(axis,axis_depth)
            elif axis.lower() == 'd':
                self.moveD(axis,axis_depth)
            else:
                self.moveB(axis,axis_depth)
        else:
            print("Introduce a valid movement")

   

    

x= Cube('../resources/cube.json')
print(x)
x.move('l2')
print('After b0: ')

