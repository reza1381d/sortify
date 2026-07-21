from pathlib import Path
import pytest
from organizer import Organizer

@pytest.mark.parametrize(
    "filename, expected",
    [
        ("pic.jpg", "Images"),
        ("book.pdf", "PDFs"),
        ("movie.mp4", "Videos"),
        ("song.mp3", "Musics"),
        ("app.exe", "Programs")
    ]
)

def test_detect_type(filename, expected):
    organizer = Organizer("Downloads")
    assert organizer.detect_type(Path(filename)) == expected