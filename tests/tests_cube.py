import pytest
from .cube import Cube


def test_md5():
    x = Cube('../resources/test.json')
    print(x.createmd5())
