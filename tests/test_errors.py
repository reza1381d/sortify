import pytest
from pathlib import Path


def test_invalid_path():

    with pytest.raises(TypeError):

        Path(None)