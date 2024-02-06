import pytest
from code_samples.lesson_40 import add
@pytest.mark.slow
def test_add():
    assert add(1, 2) == 3, "1 + 2 != 3"

