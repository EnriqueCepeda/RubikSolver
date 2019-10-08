from sortedcontainers import SortedList

class Frontier:
    
    def __init__(self):
        """This is the constructor of the Class Frontier.

        """
          
        self.List_TreeNodes = None
   
    def CreateFrontier(self):
        """This function creates a new SortedList.
        """

        self.List_TreeNodes = SortedList()

    def Insert(self,TreeNode):
        """This function adds a new node to the frontier.
        
        Arguments:
            TreeNode {Object TreeNode} -- [description]
        """
       
        self.List_TreeNodes.add(TreeNode)
    
    def Remove(self):
        """It takes the first element of the frontier (lowest ”f”)and it removes it from the fringe.
        """
        
        self.List_TreeNodes.pop(0)

    def isEmpty(self):
        """[summary]
        
        Returns:
            [boolean value] -- [It returns if it is empty or not]
        """
        
        if len(self.List_TreeNodes) == 0:
            
            return True
        
        else:
            
            return False

    