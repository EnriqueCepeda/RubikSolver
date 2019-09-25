from ctypes import c_int8
import json

class Cube:
    def __init__(self):
        self.left={}
        self.right={}
        self.up={}
        self.down={}
        self.back={}
        self.front={}

        self.positions={
            'left':{0:[0,3],1:[6,1]},
            'right':{0:[0,3],1:[0,4]},
            'up':{0:[0,6],1:[2,0]}
        }
    
    def json_decode(self,json_file):
        cube=json.loads(json_file)
        print(cube)

x= Cube()
x.json_decode('cube.json')
