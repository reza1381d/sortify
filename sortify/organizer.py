from pathlib import Path
from .logger_config import logger
from .config import IMAGE_EXTENSIONS,VIDEO_EXTENSIONS,MUSIC_EXTENSIONS,PDF_EXTENSIONS,ARCHIVE_EXTENSIONS,PROGRAM_EXTENSIONS,WORD_EXTENSIONS
import shutil


FILE_TYPES = {
        "Images" : IMAGE_EXTENSIONS,
        "Videos" : VIDEO_EXTENSIONS,
        "Musics" : MUSIC_EXTENSIONS,
        "PDFs" : PDF_EXTENSIONS,
        "Archives" : ARCHIVE_EXTENSIONS,
        "Programs" : PROGRAM_EXTENSIONS,
        "Documents": WORD_EXTENSIONS
    }


class Organizer :

    def __init__(self, folder, dry_run=False):

        self.folder = Path(folder)
        self.dry_run = dry_run
        self.stats = {}


    def show_files (self) :

        for file in self.folder.iterdir() :
            if file.is_file():
                print (file.name)


    def detect_type(self, file):
        extension = file.suffix.lower()

        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                return folder

        return "Other"


    def create_folder(self, folder_name):

        destination = self.folder / folder_name
        destination.mkdir(parents= True,exist_ok= True)


    def update_stats(self, folder_name):
        self.stats[folder_name] = self.stats.get(folder_name, 0) + 1
    
    def move_file(self, file, folder_name):

        try:
            if self.dry_run:
                print(f"{file.name} ---> {folder_name}")
                self.update_stats(folder_name)
                return
            destination_folder = self.folder / folder_name
            self.create_folder(folder_name)
            destination = destination_folder / file.name
           
            shutil.move(file, destination)
            logger.info(f"Moved {file.name} to {folder_name} -> {destination}")
            self.update_stats(folder_name)

        except Exception as e:
            logger.exception(f"failed to move {file.name}: {e}")
    
    def organize(self):

        print("Organizing files...\n")
        logger.info("Organizer started")
        files = [
            file for file in self.folder.iterdir()
            if file.is_file()
        ]
        if not files :
            print("No files found!")
            logger.info("No files found!")
            return
        total_files = len(files)
        for index, file in enumerate(files, start=1):
            folder_name = self.detect_type(file)
            print(f"[{index}/{total_files}] {file.name} --> {folder_name}")
            if folder_name != "Other":
                self.move_file(file, folder_name)
            else:
                logger.warning(f"Unknown file type: {file.name}")

        logger.info("Organizer finished")

    def show_summary(self):

        print("\n===== Sortify Summary =====")

        if not self.stats:
            print("No files processed.")
            return

        for folder, count in self.stats.items():
            print(f"{folder}: {count} files")