from queue import LifoQueue
from Cube import Cube
import os
import Frontier_SortedList
import Problem
import TreeNode
import StateSpace


class SearchStrategies():

    def __init__(self,initial_state, strategy, max_depth, depth_increment, pruning):
        self.problem = Problem.Problem(initial_state)
        self.strategy = strategy
        self.max_depth = max_depth
        self.depth_increment = depth_increment
        self.pruning = pruning


    def __f_strategy(self,node):
        """This method return a certain value of f depending on the chosen strategy for the search
        """
        if self.strategy=='UCS':
            return node.cost
        elif self.strategy=='BFS':
            return 1+node.node_depth
        elif self.strategy in {'IDS','DFS','DLS'}:
            return 1/1+node.node_depth
             

    def solution(self,node):
        """This method creates in a stack the path solution of the problem after applying the 
        search strategy
        """
        stack = LifoQueue()
        while node.parent != None:
            stack.put(node)
            node = node.parent
        stack.put(node)
        return stack


    def print_solution(self, stack):
        print("---SOLUTION---: ")
        while not stack.empty():
            node = stack.get()
            node.state.plot_cube("SOLUTION: Node "+str(node.node_depth))
            print(node.state.create_md5())


    def concrete_search (self, limit):
        frontier = Frontier_SortedList.Frontier_SortedList()
        closed = []
        initial_node = TreeNode.TreeNode(self.problem.initial_state, 0,0,None,None)
        initial_node.f = self.__f_strategy(initial_node)
        frontier.insert(initial_node)
        solution = False
        while not solution and not frontier.is_empty():
            actual_node = frontier.remove()
            #print(actual_node.state.create_md5())
            if self.problem.is_goal(actual_node.state):
                solution = True
            elif actual_node.state.create_md5() not in closed and actual_node.node_depth < limit:
                closed.insert(closed.__len__(), actual_node.state.create_md5())
                successors = StateSpace.StateSpace.successors(actual_node.state)
                for successor in successors:
                    f = self.__f_strategy(actual_node) 
                    treenode = TreeNode.TreeNode(successor[1],actual_node.cost + 1, actual_node.node_depth +1, f , actual_node)
                    frontier.insert(treenode)
        if solution:
            return self.solution(actual_node)
        else:
            return None


    def search(self):
        if self.strategy == "IDS":
            limit = self.depth_increment
        else:
            limit = self.max_depth
        solution = None
        while solution == None and limit <= self.max_depth:
            solution = self.concrete_search(limit)
            limit += self.depth_increment
        return solution
        

def ask_input():
    print("-----INTELIGENT SYSTEMS - A1-02 PROJECT-----")
    print("Which strategy do you want to select? (UCS, BFS, DLS, IDS): ")
    strategy=input()
    while strategy.upper() not in {"UCS","BFS","DLS","IDS"}:
        print("Please, select a valid stategy. ")
        strategy=input()

    print("Specify the limit of the strategy (An integer number greater than 0): ")
    limit=int(input())
    while limit <=0:
        print("Please, select a valid limit: ")
        limit=int(input())

    if strategy.upper()=="IDS":
        print("Select the increment fot the IDS strategy (An integer number greater than 0): ")
        increment=int(input())
        while increment <=0:
            print("Please, select a valid increment. ")
            increment=int(input())
    else:
        increment = 0

    print("Select the root of the json file: ")
    json_file_root = input()
    while not os.path.isfile(json_file_root):
        print("Please, select a valid json file path: ")
        json_file_root = input()

    print("Do you want to do the search using the pruning technique? (Yes/No)")
    pruning=input()
    while pruning.upper() not in {"YES", "NO", "Y", "N"}:
        print("Please, answer yes or no to the pruning question: ")
        pruning = input()

    pruning_boolean = pruning.upper() in {"YES","Y"}

    initial_cube = Cube(json_file_root)
    search_object=SearchStrategies(initial_cube, strategy, limit, increment, pruning_boolean)
    search_object.print_solution(search_object.search())


if __name__ == "__main__":
    #ask_input()
    initial_cube = Cube("resources/cube.json")
    search_object=SearchStrategies(initial_cube, "IDS", 2, 1, False)
    result = search_object.search()
    if result is not None:
        search_object.print_solution(result)
    else:
        print("No solution was found")
    
    
