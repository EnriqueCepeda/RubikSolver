from queue import LifoQueue
import os
import sys
from src.Cube import Cube as Cube
from src.Search import Frontier_SortedList
from src.Search import Problem
from src.Search import TreeNode
from src.Search import StateSpace


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

    def solution(self, node):
        """This method creates in a stack the path solution of the problem after applying the
        search strategy
        """
        stack = LifoQueue()
        while node.parent != None:
            stack.put(node)
            node = node.parent
        stack.put(node)
        return stack

    def output_solution(self, list_solution):
        with open("src/resources/solution.out", "w") as file:
            file.write("Strategy: " + str(self.strategy))
            file.write("\n Max Depth: " + str(self.max_depth))
            file.write("\n Depth Increment: " + str(self.depth_increment))
            file.write("\n Pruning: " + str(self.pruning))
            file.write("\n ---SOLUTION---: ")
            for node in list_solution:
                file.write("\n\n ID: " + str(node.id))
                if node.last_action != None:
                    file.write("\n Action: " + str(node.last_action))
                file.write("\n Cost: " + str(node.cost))
                file.write("\n Depth: " + str(node.node_depth))
                file.write("\n Heuristic: " + str(node.state.entropy()))
                file.write("\n F value: " + str(node.f))
                file.write("\n Node:" + str(node.state.create_md5()))
            file.write("\n TOTAL COST: " + str(node.cost))

    def print_solution(self, stack):
        list_solution = []
        print("---SOLUTION---: ")
        while not stack.empty():
            node = stack.get()
            node.state.plot_cube(
                "SOLUTION: Node [" + str(node.id) + "] at depth " + str(node.node_depth)
            )
            if node.last_action != None:
                print("Next action: ", node.last_action)
            print("[" + str(node.id) + "] " + str(node.state.create_md5()))
            list_solution.append(node)
        print("TOTAL COST: ", node.cost)
        return list_solution

    def concrete_search(self, limit):
        frontier = Frontier_SortedList.Frontier_SortedList()
        closed = {}
        list_nodes = []
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
        frontier.insert(initial_node)
        id = 1
        solution = False
        while not solution and not frontier.is_empty():
            actual_node = frontier.remove()
            pruned = False
            if self.problem.is_goal(actual_node.state):
                solution = True
            else:
                if self.pruning == 1:
                    pruned = self.check_node_pruning1(actual_node, closed)
                    if not pruned:
                        closed[actual_node.state.create_md5()] = actual_node.f

                if self.pruning in [0, 1]:
                    if not pruned:
                        if actual_node.node_depth < limit:
                            frontier, id = self.expand_node(id, actual_node, frontier)

                if self.pruning == 2:
                    if actual_node.node_depth < limit:
                        list_nodes, id = self.expand_node2(id, actual_node, list_nodes)
                        for node in list_nodes:
                            md5 = node.state.create_md5()
                            if md5 not in closed:
                                closed[md5] = node.f
                                frontier.insert(node)
                            elif md5 in closed:
                                if closed[md5] > node.f:
                                    closed[md5] = node.f
                                    frontier.insert(node)
                        list_nodes.clear()
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

    def expand_node2(self, id, actual_node, node_list):
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
    def check_node_pruning1(self, actual_node, closed):
        actual_md5 = actual_node.state.create_md5()
        if (actual_md5 not in closed) or (abs(actual_node.f) < abs(closed[actual_md5])):
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
            print("Please, select a valid stategy.\n")
            strategy = input().upper()
        if strategy == "DFS":
            limit = 10000
            strategy = "DLS"
        else:
            limit = self.ask_integer(
                "Specify the limit of the strategy (An integer number greater than 0): ",
                "Please, select a valid limit:\n",
            )

        if strategy == "IDS":
            increment = self.ask_integer(
                "You are using IDS strategy, specify the limit (An integer number greater than 0): ",
                "Please, select a valid increment.\n ",
            )
        else:
            increment = 1

        print("Select the root of the json file: ")
        json_file_root = input()
        while not os.path.isfile(json_file_root):
            print("Please, select a valid json file path: ")
            json_file_root = input()

        print("Do you want to do the search using the pruning technique? (Yes/No)")
        pruning = input().upper()
        while pruning not in {"YES", "NO", "Y", "N"}:
            print("Please, answer yes or no to the pruning question: ")
            pruning = input().upper()

        pruning_boolean = pruning in {"YES", "Y"}

        return strategy, limit, increment, json_file_root, pruning_boolean

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


if __name__ == "__main__":
    try:
        # strategy, limit, increment, json_path, pruning = SearchStrategies.user_interface()
        # initial_cube = Cube.Cube(json_path)
        initial_cube = Cube.Cube("src/resources/ejemplo_2x2.json")
        # search_object = SearchStrategies(initial_cube, strategy, limit, increment, pruning)
        search_object = SearchStrategies(initial_cube, "DLS", 6, 1, 1)
        result = search_object.search()
        if result is not None:
            list_result = search_object.print_solution(result)
            search_object.output_solution(list_result)
        else:
            print("No solution was found")
    except KeyboardInterrupt as kb:
        sys.exit(1)
    finally:
        print("Thanks for using our software. Bye!")
