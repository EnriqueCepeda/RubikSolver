from sortedcontainers import SortedList


class Frontier_SortedList():

    def __init__(self):
        """This is the constructor of the Class Frontier. 

        """
        self.list_TreeNodes = SortedList(
            key=lambda treenode: treenode.f)

    def insert(self, TreeNode):
        """This function adds a new TreeNode in the frontier and sort the list depending on the value of "f" in ascendent.
        """

        self.list_TreeNodes.add(TreeNode)

    def remove(self):
        """It takes the first element of the frontier (lowest "f") and it removes it from the frontier.
        """

        return self.list_TreeNodes.pop(0)

    def is_empty(self):
        """This function checks if the Sort List is empty or not.
        """
        if len(self.list_TreeNodes) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self.list_TreeNodes)
