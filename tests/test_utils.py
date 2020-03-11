"""
To test utility functions module.
"""
from gaikwad411_greet.gaikwad411_greet import utils


def test_greet():
    assert utils.greet() == 'Hello World!'
