import Frontier_SortedList as Frontier_SortedList
import TreeNode as TreeNode
import Cube as Cube

initial_cube = Cube.Cube("src/resources/heuristic_example.json")
frontier = Frontier_SortedList.Frontier_SortedList()
initial_node = TreeNode.TreeNode(
    6, initial_cube, 0, 0, 3.5, None, None
)
initial_node = TreeNode.TreeNode(
    0, initial_cube, 0, 0, 3.5, None, None
)
initial_node_2 = TreeNode.TreeNode(
    3, initial_cube, 0, 0, 3.5, None, None
)
initial_node_3 = TreeNode.TreeNode(
    -1, initial_cube, 0, 0, 3.5, None, None
)
initial_node_4 = TreeNode.TreeNode(
    57000, initial_cube, 0, 0, 3.5, None, None
)
frontier.insert(initial_node)
frontier.insert(initial_node_2)
frontier.insert(initial_node_3)
frontier.insert(initial_node_4)
initial_node = frontier.remove()
print(initial_node.id)

count = 1

for i in range(1717):
    print(1/(1+i))
