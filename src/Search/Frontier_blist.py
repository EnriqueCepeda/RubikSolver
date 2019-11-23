from blist import sortedlist


class Frontier_blist():


    def __init__(self):
        """This is the constructor of the Class Frontier. 
        """
        self.list_TreeNodes = sortedlist(key=lambda treenode: treenode.f)

    def insert(self,treeNode):
        self.list_TreeNodes.add(treeNode)

    def remove(self):
        self.list_TreeNodes.pop(0)
    
    def is_empty(self):
        if len(self.list_TreeNodes) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self.list_TreeNodes)

