import random

class TreeNode():

    def __init__(self,state,cost,node_depth,parent=None):
        
        self.state = state
        self.cost = cost
        self.node_depth = node_depth
        self.f = random.randrange(1,10000,1)
        self.parent = parent


