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

    def __init__(self, folder, dry_run=False, verbose=True):

        self.folder = Path(folder)
        self.dry_run = dry_run
        self.stats = {
            "Images": 0,
            "Videos": 0,
            "Musics": 0,
            "PDFs": 0,
            "Archives": 0,
            "Programs": 0,
            "Documents": 0,
            "Other": 0
        }
        self.verbose = verbose


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
        self.stats[folder_name] += 1
    
    def move_file(self, file, folder_name):

        try:
            if self.dry_run:
                if self.verbose:
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

        if self.verbose:
            print("Organizing files...\n")
        logger.info("Organizer started")
        files = [
            file for file in self.folder.iterdir()
            if file.is_file()
        ]
        if not files :
            if self.verbose:
                print("No files found!")
            logger.info("No files found!")
            return
        total_files = len(files)
        for index, file in enumerate(files, start=1):
            folder_name = self.detect_type(file)
            if self.verbose:
                print(f"[{index}/{total_files}] {file.name} --> {folder_name}")
            if folder_name != "Other":
                self.move_file(file, folder_name)
            else:
                self.update_stats("Other")
                logger.warning(f"Unknown file type: {file.name}")

        logger.info("Organizer finished")

    def show_summary(self):
        print("\n===== Sortify Summary =====")

        if not self.stats:
            print("No files processed.")
            return

        for folder, count in self.stats.items():
            print(f"{folder}: {count} files")