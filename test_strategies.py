import pytest
import src.Search as SearchStrategies
import src.Cube as Cube
import src.TreeNode as TreeNode


test_file = 'src/resources/test.json'


def test_pruning():
    cube = Cube.Cube(test_file)
    treenode = TreeNode.TreeNode(cube, 0, 0, 0, None, None)
    closed = {treenode.state.create_md5(): treenode.f}
    pruned = SearchStrategies.SearchStrategies.check_node_pruning(
        treenode, closed)
    assert pruned

def test_UCS():
    initial_cube = Cube.Cube(test_file)
    search_UCS = SearchStrategies.SearchStrategies(
        initial_cube, "UCS", 2, 1, True)
    result = search_UCS.search()
    while not result.empty():
        node = result.get()
    assert node.node_depth == 2
    
def test_DLS():
    initial_cube = Cube.Cube(test_file)
    search_UCS = SearchStrategies.SearchStrategies(
        initial_cube, "DLS", 2, 1, True)
    result = search_UCS.search()
    while not result.empty():
        node = result.get()
    assert node.node_depth == 2

def test_IDS():
    initial_cube = Cube.Cube(test_file)

    search_IDS = SearchStrategies.SearchStrategies(
        initial_cube, "IDS", 10, 1, True)
    solution_IDS = search_IDS.search()
    while solution_IDS.not_empty:
        node = solution_IDS.get()
    IDS_solution_depth = node.node_depth
    search_BFS = SearchStrategies.SearchStrategies(
        initial_cube, "BFS", 10, 1, True)
    solution_BFS = search_BFS.search()
    while solution_BFS.not_empty:
        node = solution_BFS.get()
    BFS_solution_depth = node.node_depth

    assert IDS_solution_depth == BFS_solution_depth
