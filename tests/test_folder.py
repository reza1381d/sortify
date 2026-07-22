from pathlib import Path
from sortify.organizer import Organizer

def test_create_folder(organizer):

    organizer.create_folder("Images")

    assert (organizer.folder / "Images").exists()