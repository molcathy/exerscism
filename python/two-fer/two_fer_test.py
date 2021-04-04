import pytest
from two_fer import twofer


def test_twofer():
    assert twofer('Alice') == 'One for Alice, one for me.'
    assert twofer() == 'One for you, one for me.'

