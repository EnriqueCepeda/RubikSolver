import pytest
from src.Search.Search import SearchStrategies
from src.Cube import Cube
from src.Search import TreeNode

test_file = "src/resources/test.json"


def test_pruning():
    cube = Cube.Cube(test_file)
    treenode = TreeNode.TreeNode(
        id=0, state=cube, cost=0, node_depth=0, f=0, parent=None, last_action=None
    )
    closed = {treenode.state.create_md5(): treenode.f}
    pruned = SearchStrategies.check_node_pruning_1st_prune(treenode, closed)
    assert pruned


