import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from .organizer import Organizer

root = tk.Tk()

root.title("Sortify")
root.geometry("500x250")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

title = tk.Label(
    frame,
    text="Sortify",
    font=("Segoe UI", 20, "bold")
)

title.pack(pady=(0, 5))


subtitle = tk.Label(
    frame,
    text="Organize your files in one click",
    font=("Segeo UI", 10)
)

subtitle.pack(pady=(0, 20))


folder_path = tk.StringVar()

def browse_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_path.set(folder)


folder_frame = tk.Frame(frame)
folder_frame.pack(fill="x", pady=10)


def organize_files():
    folder = folder_path.get()

    if not folder:
        messagebox.showwarning(
            "NO Folder",
            "Please select a folder first."
        )
        return

    organizer = Organizer(
        folder,
        verbose=False
        )

    organizer.organize()
    summary = ""

    for folder, count in organizer.stats.items():
        if count > 0:
            summary += f"{folder}: {count} files\n"


    messagebox.showinfo(
        "Sortify summary",
        summary if summary else "No files processed."
    )



organize_button = tk.Button(
    frame,
    text="Organize Files",
    command=organize_files,
    width=20,
    height=2
)

organize_button.pack(pady=20)


folder_entry = tk.Entry(
    folder_frame,
    textvariable= folder_path
)

folder_entry.pack(
    side= "left",
    fill= "x",
    expand=True
)


browse_button = tk.Button(
    folder_frame,
    text= "Browse",
    command= browse_folder
)

browse_button.pack(
    side= "left",
    padx=10
)


root.mainloop()