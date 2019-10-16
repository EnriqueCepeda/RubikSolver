from sortedcontainers import SortedSet


class Frontier_SortedSet():
    def __init__(self):
        """This is the constructor of the Class Frontier. 
        """
        self.List_TreeNodes = SortedSet(key=lambda h: h.f)


    def insert(self,TreeNode):
        """This function adds a new TreeNode in the frontier and sort the list depending on the value of "f" in ascendent.

        """

        self.List_TreeNodes.add(TreeNode)

    def remove(self):
        """It takes the first element of the frontier (lowest "f") and it removes it from the frontier.
        """

        self.List_TreeNodes.pop(0)
    
    def is_empty(self):
        """This function checks if the Sort List is empty or not.
        """

        if len(self.List_TreeNodes) == 0:

            return True
        else:
            
            return False
