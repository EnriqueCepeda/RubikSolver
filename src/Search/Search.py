from queue import LifoQueue
import os
import sys
from src.Cube import Cube as Cube
from src.Search import Frontier_SortedList
from src.Search import Problem
from src.Search import TreeNode
from src.Search import StateSpace
import time


class SearchStrategies:
    def __init__(self, initial_state, strategy, max_depth, depth_increment, pruning):
        self.problem = Problem.Problem(initial_state)
        self.strategy = strategy
        self.max_depth = max_depth
        self.depth_increment = depth_increment
        self.pruning = pruning

    def __f_strategy(self, node):
        """This method return a certain value of f depending on the chosen strategy for the search
        """
        if self.strategy == "UCS":
            return node.cost
        elif self.strategy == "BFS":
            return node.node_depth
        elif self.strategy in {"IDS", "DLS"}:
            return -node.node_depth
        elif self.strategy == "GREEDY":
            return node.state.entropy()
        elif self.strategy == "A*":
            return node.state.entropy() + node.cost

    def solution(self, solution_node):
        """
        This method stores the path solution in a list, working as a lifo queue.
        Extracts the solution from the solution node, from the first to the last
        """
        solution_path = []
        while solution_node.parent != None:
            solution_path.append(solution_node)
            solution_node = solution_node.parent
        solution_path.append(solution_node)
        return solution_path[::-1]

    def save_solution(self, solution_path, file_path):
        """
        This function outputs the solution to a file (filepath) by means of the argument list_solution
        Arguments:
            list_solution {List} -- contains the solution node path from first to last
            file_path {String} -- contains the file_path were the solution is saved
        """
        node_info = ""
        with open(file_path, "w") as file:
            file.write(
                "Strategy: "
                + str(self.strategy)
                + "\n Max Depth: "
                + str(self.max_depth)
                + "\n Depth Increment: "
                + str(self.depth_increment)
                + "\n Pruning: "
                + str(self.pruning)
                + "\n ---SOLUTION---: "
            )
            for node in solution_path:
                node_info = "\n\n ID: " + str(node.id)
                if node.last_action != None:
                    node_info += "\n Action: " + str(node.last_action)
                node_info += (
                    "\n Cost: "
                    + str(node.cost)
                    + "\n Depth: "
                    + str(node.node_depth)
                    + "\n Heuristic: "
                    + str(node.state.entropy())
                    + "\n F value: "
                    + str(node.f)
                    + "\n Node: "
                    + str(node.state.create_md5())
                )
                file.write(node_info)
                node_info = ""

            file.write(
                "\n TOTAL COST: " + str(solution_path[len(solution_path) - 1].cost)
            )

    def print_solution(self, solution_path):
        """
        Outputs the solution by the terminal and also draws in the screen the states composing the solution
        
        Arguments:
            solution_path {List} -- contains the path of nodes of the solution from the first to the last
        """
        print("---SOLUTION---: ")
        for node in solution_path:
            node.state.plot_cube(
                "SOLUTION: Node [" + str(node.id) + "] at depth " + str(node.node_depth)
            )
            if node.last_action != None:
                print("Next action: ", node.last_action)
            print("[" + str(node.id) + "] " + str(node.state.create_md5()))

        print("\n TOTAL COST: ", solution_path[len(solution_path) - 1].cost)

    def concrete_search(self, limit):
        """ This method does executes the search algorithm for all the strategies
        
        Arguments:
            limit {Integer} -- Is the maximum limit of the tree, if the depth is higher than
                               the limit, it prunes that node
        
        Returns:
            List or None -- Returns a list if the cube has a result, else returns None
        """
        frontier = Frontier_SortedList.Frontier_SortedList()
        closed = {}
        initial_node = TreeNode.TreeNode(
            id=0,
            state=self.problem.initial_state,
            cost=0,
            node_depth=0,
            f=None,
            parent=None,
            last_action=None,
        )
        initial_node.f = self.__f_strategy(initial_node)
        id = 1
        frontier.insert(initial_node)
        solution = False
        while not solution and not frontier.is_empty():
            actual_node = frontier.remove()
            pruned = False
            if self.problem.is_goal(actual_node.state):
                solution = True
            else:
                if self.pruning == 1:
                    pruned = self.check_node_pruning_1st_prune(actual_node, closed)
                    if not pruned:
                        closed[actual_node.state.create_md5()] = abs(actual_node.f)

                if self.pruning in [0, 1]:
                    if not pruned:
                        if actual_node.node_depth < limit:
                            frontier, id = self.expand_node(id, actual_node, frontier)

                if self.pruning == 2:
                    if actual_node.node_depth < limit:
                        list_nodes, id = self.expand_node_2nd_prune(id, actual_node)
                        for node in list_nodes:
                            md5 = node.state.create_md5()
                            if md5 not in closed or closed[md5] > abs(node.f):
                                closed[md5] = abs(node.f)
                                frontier.insert(node)
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
        while solution is None and limit <= self.max_depth:
            solution = self.concrete_search(limit)
            limit += self.depth_increment
        return solution

    def expand_node(self, id, actual_node, frontier):
        successors = StateSpace.StateSpace.successors(actual_node.state)
        for successor in successors:
            treenode = TreeNode.TreeNode(
                id=id,
                state=successor[1],
                cost=actual_node.cost + 1,
                node_depth=actual_node.node_depth + 1,
                f=actual_node.f,  # this will be changed in the next operation
                parent=actual_node,
                last_action=successor[0],
            )
            treenode.f = self.__f_strategy(treenode)
            frontier.insert(treenode)
            id += 1
        return frontier, id

    def expand_node_2nd_prune(self, id, actual_node):
        node_list = []
        successors = StateSpace.StateSpace.successors(actual_node.state)
        for successor in successors:
            treenode = TreeNode.TreeNode(
                id=id,
                state=successor[1],
                cost=actual_node.cost + 1,
                node_depth=actual_node.node_depth + 1,
                f=actual_node.f,  # this will be changed in the next operation
                parent=actual_node,
                last_action=successor[0],
            )
            treenode.f = self.__f_strategy(treenode)
            node_list.append(treenode)
            id += 1
        return node_list, id

    @classmethod
    def check_node_pruning_1st_prune(self, actual_node, closed):
        actual_md5 = actual_node.state.create_md5()
        if (actual_md5 not in closed) or (abs(actual_node.f) < closed[actual_md5]):
            return False
        else:
            return True

    @classmethod
    def user_interface(self):
        print("-----INTELIGENT SYSTEMS - A1-02 PROJECT-----")
        print(
            "Which strategy do you want to select? (UCS, BFS, DLS, IDS, DFS, GREEDY, A*): "
        )
        strategy = input().upper()
        while strategy not in {"UCS", "BFS", "DLS", "IDS", "DFS", "GREEDY", "A*"}:
            print("Please, select a valid stategy.")
            strategy = input().upper()
        if strategy == "DFS":
            limit = 10000
            strategy = "DLS"
        else:
            limit = self.ask_integer(
                "Specify the limit of the strategy (An integer number greater than 0): ",
                "Please, select a valid limit:",
            )

        if strategy == "IDS":
            increment = self.ask_integer(
                "You are using IDS strategy, specify the limit (An integer number greater than 0): ",
                "Please, select a valid increment. ",
            )
        else:
            increment = 1

        print("Select the root of the json file: ")
        json_file_root = input()
        while not os.path.isfile(json_file_root):
            print("Please, select a valid json file path: ")
            json_file_root = input()

        pruning = self.ask_pruning(
            "Do you want to do the search using any pruning technique? (0,1,2): ",
            "Please, answer any of these numbers:(0,1,2) to the pruning question: ",
        )

        return strategy, limit, increment, json_file_root, pruning

    @classmethod
    def ask_integer(self, ask_sentence, askagain_sentence):
        print(ask_sentence)
        continuar = False
        while continuar == False:
            try:
                user_input = int(input())
                while user_input <= 0:
                    print(askagain_sentence)
                    user_input = int(input())
                continuar = True
            except ValueError:
                print(askagain_sentence)
        return user_input

    @classmethod
    def ask_pruning(self, ask_sentence, askagain_sentence):
        print(ask_sentence)
        continuar = False
        while continuar == False:
            try:
                user_input = int(input())
                while user_input not in [0, 1, 2]:
                    print(askagain_sentence)
                    user_input = int(input())
                continuar = True
            except ValueError:
                print(askagain_sentence)
        return user_input


if __name__ == "__main__":
    try:
        strategy, limit, increment, json_path, pruning = SearchStrategies.user_interface()
        initial_cube = Cube.Cube(json_path)
        search_object = SearchStrategies(
            initial_cube, strategy, limit, increment, pruning
        )
        initial_time = time.time_ns()
        result = search_object.search()
        final_time = time.time_ns()
        if result is not None:
            search_object.print_solution(result)
            search_object.save_solution(result, "src/resources/solution.out")
            print(
                "Time searching: "
                + str((final_time - initial_time) / 1000000000)
                + " s"
            )
        else:
            print("No solution was found")
    except KeyboardInterrupt as kb:
        sys.exit(1)
    finally:
        print("Thanks for using our software. Bye!")
