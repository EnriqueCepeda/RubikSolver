import random

class TreeNode():

    def __init__(self,parent,state,cost,node_depth):
        
        self.parent = parent
        self.state = state
        self.cost = cost
        self.node_depth = node_depth
        self.f = random.randrange(1,10000,1)


