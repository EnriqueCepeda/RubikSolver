import Frontier_SortedList
import Problem 
import TreeNode


class SearchStrategies:


    def __init__(self,initial_state):
        self.problem = Problem(initial_state)

    def __f_strategy(self,strategy,node):
        if strategy=='UCS':
            return node.f
        elif strategy=='BFS':
            return 1+node.depth
        elif strategy in {'IDS','DFS','DLS'}:
            return 1/1+node.depth
             
    def solution(self,node):
        pass

    def concrete_search (self,strategy,max_depth):
        frontier = Frontier_SortedList()
        initial_node = TreeNode(self.problem.initial_state,0,0,0)
        frontier.insert(initial_node)
        solution = False
        while solution == False and frontier.is_empty()==False:
            actual_node = frontier.pop()
            if self.problem.is_goal(actual_node.state()):
                solution = True
            else:
                successors = self.problem.stateSpace.successors(actual_node.state)
                for successor in successors:
                    f = self.__f_strategy(strategy,actual_node) 
                    treenode = TreeNode(successor[1],actual_node.cost + 1, actual_node.depth +1, f , actual_node)
                    frontier.insert(treenode)
        if solution:
            return solution(actual_node)
        else:
            return None

    def search(self,problem,strategy,max_depth,depth_increment):
        actual_depth = depth_increment
        solution = None
        while solution == None and actual_depth <= max_depth:
            solution = self.concrete_search(strategy,actual_depth)
            actual_depth += depth_increment
        return solution