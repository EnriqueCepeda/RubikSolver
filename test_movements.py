import pytest
from src.Cube import Cube

test_file = 'src/resources/ejemplo10x10.json'
def test_importing_json():
    x=Cube(test_file)
    x.move('l3')    
    x.move('D1')
    x.move('l1')
    assert x.create_md5() == '3072cd153434334e62487aa2c52d0b1c'
    x.move('d0')
    assert x.create_md5() == 'dab05f73e4ed15c2394f1712f9dc4fca'
    x.move('B0')
    x.move('b5')
    assert x.create_md5() == '8aef8f1a6b6d427fb55581dee01e2557'
    x.move('l2')
    x.move('d1')    
    assert x.create_md5() == 'e8682bbb2e6fabf5971e4b471ae2d46d'