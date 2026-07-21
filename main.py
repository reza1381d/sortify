from organizer import Organizer
import argparse


parser = argparse.ArgumentParser(
    description= "Organize your files automatically"
)

parser.add_argument(
    "--folder",
    help="folder path to organize",
    required=True
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="show changes without moving files"
)

args = parser.parse_args()




organizer = Organizer(
    args.folder,
    args.dry_run)
#organizer.show_files()
organizer.organize()
organizer.show_summary()
