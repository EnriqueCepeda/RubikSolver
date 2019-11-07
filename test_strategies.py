import pytest
from src.Search import SearchStrategies
from src.Cube import Cube
import src.TreeNode as TreeNode

def test_pruning():
    cube = Cube("test.json")
    treenode = TreeNode(cube, 0, 0, 0, None, None)
    closed = {cube.create_md5(): cube.f}
    successors = SearchStrategies.check_node_pruning(treenode, closed)
    assert successors.is_empty()


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
