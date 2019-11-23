import pytest
from src.Cube.Cube import Cube

test_file = "src/resources/ejemplo_10x10.json"


def test_importing_json():
    x = Cube(test_file)
    assert x.create_md5() == "69db38e2ce96d3044adc00e612a810b0"
    x.move("l3")
    assert x.create_md5() == "130d0d212b8cc15f375b1b0f2cdf42ad"
    x.move("D1")
    assert x.create_md5() == "d83b0f604f0fbdd646497bcc400cb701"
    x.move("l1")
    assert x.create_md5() == "3072cd153434334e62487aa2c52d0b1c"
    x.move("d0")
    assert x.create_md5() == "dab05f73e4ed15c2394f1712f9dc4fca"
    x.move("B0")
    assert x.create_md5() == "ff8a8cd7a7af5da72edfad5d0a801a97"
    x.move("b5")
    assert x.create_md5() == "8aef8f1a6b6d427fb55581dee01e2557"
    x.move("l2")
    assert x.create_md5() == "151faa80eb7b01fa8db7e8129778de10"
    x.move("d1")
    assert x.create_md5() == "e8682bbb2e6fabf5971e4b471ae2d46d"

