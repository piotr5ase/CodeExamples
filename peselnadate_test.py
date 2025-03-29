import pytest
from peselnadate import checkpesel
def test():
    assert "1953.1.12" ==checkpesel("53012456424")