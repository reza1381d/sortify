from pathlib import Path
from sortify.organizer import Organizer

def test_move_file(organizer):

    file = organizer.folder / "song.mp3"

    file.write_text("test")

    organizer.move_file(file, "Musics")

    assert (organizer.folder / "Musics" / "song.mp3").exists()