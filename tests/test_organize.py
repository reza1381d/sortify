from pathlib import Path
from sortify.organizer import Organizer


def test_organize(tmp_path):

    image = tmp_path / "photo.jpg"
    music = tmp_path / "song.mp3"

    image.write_text("test")
    music.write_text("test")

    organizer = Organizer(tmp_path)

    organizer.organize()

    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "Musics" / "song.mp3").exists()