import json
import hashlib
from numpy import array, rot90, nditer
from math import sqrt
import string

class Cube:
    def __init__(self,json_file):

        with open(json_file, 'r') as f:
            distros_dict = json.load(f)
        self.left = array(distros_dict['LEFT'],dtype='int8')
        self.right= array(distros_dict['RIGHT'],dtype='int8')
        self.up= array(distros_dict['UP'],dtype='int8')
        self.down= array(distros_dict['DOWN'],dtype='int8')
        self.back= array(distros_dict['BACK'],dtype='int8')
        self.front= array(distros_dict['FRONT'],dtype='int8')
        self.n = sqrt(self.left.size)
    
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
        pass

    def moveD(self,*args):
        pass
    
    def moveB(self,*args):
        pass

    def move(self, movement):

        axis = movement[:1]
        axis_depth = movement[1:]
        if axis.islower == 'l':
            self.moveL(axis,axis_depth)
        elif axis.islower== 'd':
            self.moveD(axis,axis_depth)
        else:
            self.moveB(axis,axis_depth)

        



x= Cube('cube.json')

