
class TreeNode():

    def __init__(self, state, cost, node_depth, f, parent, last_action):
        self.state = state
        self.cost = cost
        self.node_depth = node_depth
        self.f = f
        self.parent = parent
        self.last_action = last_action
