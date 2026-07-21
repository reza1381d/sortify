import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from organizer import Organizer


@pytest.fixture
def organizer(tmp_path):
    return Organizer(tmp_path)