from sortify.organizer import Organizer


def test_dry_run(organizer):

    file = organizer.folder / "photo.jpg"

    file.write_text("test")

    organizer.dry_run = True

    organizer.move_file(file, "Images")

    assert file.exists()
    assert not (organizer.folder / "Images" / "photo.jpg").exists()