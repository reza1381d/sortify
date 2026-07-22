import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

import threading

from .organizer import Organizer



class SortifyGUI:


    def __init__(self, root):

        self.root = root

        self.root.title("Sortify")
        self.root.geometry("500x400")


        self.folder_path = tk.StringVar()
        self.status_text = tk.StringVar()


        self.create_widgets()



    def create_widgets(self):


        frame = tk.Frame(
            self.root,
            padx=20,
            pady=20
        )

        frame.pack(
            fill="both",
            expand=True
        )


        title = tk.Label(
            frame,
            text="Sortify",
            font=("Segoe UI",20,"bold")
        )

        title.pack(
            pady=(0,5)
        )


        subtitle = tk.Label(
            frame,
            text="Organize your files in one click",
            font=("Segoe UI",10)
        )

        subtitle.pack(
            pady=(0,20)
        )


        folder_frame = tk.Frame(frame)

        folder_frame.pack(
            fill="x",
            pady=10
        )


        entry = tk.Entry(
            folder_frame,
            textvariable=self.folder_path
        )

        entry.pack(
            side="left",
            fill="x",
            expand=True
        )


        browse = tk.Button(
            folder_frame,
            text="Browse",
            command=self.browse_folder
        )

        browse.pack(
            side="left",
            padx=10
        )


        self.organize_button = tk.Button(
            frame,
            text="Organize Files",
            command=self.organize_files,
            width=20,
            height=2
        )

        self.organize_button.pack(
            pady=20
        )


        self.progress = ttk.Progressbar(
            frame,
            length=350,
            mode="determinate"
        )

        self.progress.pack(
            pady=10
        )


        status = tk.Label(
            frame,
            textvariable=self.status_text
        )

        status.pack()


        self.result_label = tk.Label(
            frame,
            text="",
            justify="left",
            anchor="w"
        )

        self.result_label.pack(
            pady=10
        )




    def browse_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.folder_path.set(folder)




    def organize_files(self):

        folder = self.folder_path.get()


        if not folder:

            messagebox.showwarning(
                "No Folder",
                "Please select a folder first."
            )

            return


        self.organize_button.config(
            state="disabled"
        )


        self.progress["value"] = 0


        self.status_text.set(
            "Starting..."
        )


        thread = threading.Thread(
            target=self.run_organizer,
            args=(folder,)
        )


        thread.start()




    def run_organizer(self, folder):


        organizer = Organizer(

            folder,

            verbose=False,

            progress_callback=self.update_progress

        )


        organizer.organize()


        summary = ""


        for folder,count in organizer.stats.items():

            if count > 0:

                summary += (
                    f"{folder}: {count} files\n"
                )



        self.root.after(

            0,

            lambda:
            self.result_label.config(
                text=summary
            )

        )


        self.root.after(

            0,

            lambda:
            self.status_text.set(
                "Completed ✓"
            )

        )


        self.root.after(

            0,

            lambda:
            self.organize_button.config(
                state="normal"
            )

        )




    def update_progress(
        self,
        current,
        total
    ):


        percent = (
            current / total
        ) * 100


        self.root.after(

            0,

            lambda:
            self.progress.config(
                value=percent,
                maximum=100
            )

        )


        self.root.after(

            0,

            lambda:
            self.status_text.set(
                f"Processing {current}/{total}"
            )

        )




def run():

    root = tk.Tk()

    app = SortifyGUI(root)

    root.mainloop()



if __name__ == "__main__":

    run()