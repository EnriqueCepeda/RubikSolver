import json
import hashlib
from numpy import array, rot90, nditer, copy
from math import sqrt
 
class Cube:
    def __init__(self,json_file):

        with open(json_file, 'r') as f:
            cube_configuration = json.load(f)
        self.left = array(cube_configuration['LEFT'],dtype='int8')
        self.right= array(cube_configuration['RIGHT'],dtype='int8')
        self.up= array(cube_configuration['UP'],dtype='int8')
        self.down= array(cube_configuration['DOWN'],dtype='int8')
        self.back= array(cube_configuration['BACK'],dtype='int8')
        self.front= array(cube_configuration['FRONT'],dtype='int8')
        self.n = int(sqrt(self.left.size))
    
    def create_md5(self):
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

        axis = args[0]
        axis_depth = args[1]

        if axis.islower():
            aux_front = self.front[:,axis_depth].copy()
            aux_down = self.down[:,axis_depth].copy()
            aux_back = self.back[:,axis_depth].copy()

            self.down[:,axis_depth] = aux_back
            self.back[:,axis_depth] = self.up[:,self.n - 1 - axis_depth]
            self.up[:,self.n - 1 - axis_depth] = aux_front
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
        pass
    
    def moveB(self,*args):
        pass

    def move(self, movement):

        axis = movement[:1]
        axis_depth = int(movement[1:])
        if axis.lower() == 'l':
            self.moveL(axis,axis_depth)
        elif axis.lower() == 'd':
            self.moveD(axis,axis_depth)
        else:
            self.moveB(axis,axis_depth)

        



x= Cube('../resources/cube.json')
print(x.front)
print(x.down)
print(x.back)
print(x.up)
print(x.left)
x.move('l1')
print('')
print(x.front)
print(x.down)
print(x.back)
print(x.up)
print(x.left)
