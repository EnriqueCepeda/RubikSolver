import pytest
import os 
from cube.Cube import Cube

test_file = '../resources/test.json'
def test_valid_movements():
    """
    This test checks if the list of valid movements in a 3x3x3 cube is done properly
    """
    x = Cube(test_file)
    if x.n == 3:
        assert x.valid_movements() == ['B0', 'B1', 'B2', 'b0', 'b1', 'b2', 'D0', 'D1', 'D2', 'd0', 'd1', 'd2', 'L0', 'L1', 'L2', 'l0', 'l1', 'l2']

def test_b0_B0():
    """
    This test checks if a cube returns to its initial configuration after two complementary movements are done
    """
    x = Cube(test_file)
    initial_md5 = x.create_md5()

    x.move('B0')
    assert x.create_md5() != initial_md5

    x.move('b0')
    assert x.create_md5() == initial_md5

def test_360():
    """
    This test checks if a cube returns to its initial configuration after four movements of the same type 
    are done
    """
    x = Cube(test_file)
    initial_md5 = x.create_md5()

    for i in range(4):
        x.move('D2')

    assert x.create_md5() == initial_md5

def test_360_all_movements():
    """
    This test checks if a cube returns to its initial position after four movements of the same type 
    for each of the valid movements of the cube
    """
    x = Cube(test_file)
    initial_md5 = x.create_md5()

    for movement in x.valid_movements():
        for i in range(4):
            x.move(movement)

    assert x.create_md5() == initial_md5

def test_json_convert():
    pass
