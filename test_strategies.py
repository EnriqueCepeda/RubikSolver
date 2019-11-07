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


def test_BFS():
    pass


def test_DFS():
    pass


def test_UCS():
    pass


def test_IDS():
    pass


def test_DLS():
    pass
