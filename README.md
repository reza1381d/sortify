# 📂 Sortify

A Python application that automatically organizes files into categorized folders based on their file extensions.

Sortify provides both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** for an easy and efficient file organization experience.

---

## ✨ Features

* Organize files automatically by type
* Supports:

  * Images
  * Videos
  * Music
  * PDFs
  * Archives
  * Programs
  * Documents
* Command-Line Interface (CLI)
* Graphical User Interface (GUI)
* Dry-run mode for previewing changes
* File processing statistics
* Progress tracking in GUI
* Background processing with threading
* Logging system
* Automated tests with pytest
* Windows executable support with PyInstaller

---

## 📸 Screenshots

*Add screenshots of the GUI here.*

---

## 📁 Project Structure

```text
Sortify/
│
├── sortify/
│   ├── organizer.py
│   ├── gui.py
│   ├── config.py
│   ├── logger_config.py
│   └── __main__.py
│
├── tests/
│
├── assets/
│   └── sortify.ico
│
├── run_sortify.py
├── run_gui.py
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>

cd Sortify
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -e .
```

---

## ▶️ Usage

## Command-Line Interface (CLI)

Organize a folder:

```bash
python run_sortify.py --folder "C:\Users\YourName\Downloads"
```

Preview changes without moving files:

```bash
python run_sortify.py --folder "C:\Users\YourName\Downloads" --dry-run
```

---

## Graphical User Interface (GUI)

Run the GUI version:

```bash
python run_gui.py
```

Select a folder, click **Organize Files**, and Sortify will automatically organize your files while showing progress and results.

---

## 📦 Executable Version

Windows executable files can be created using PyInstaller:

GUI version:

```bash
pyinstaller --onefile --windowed --icon=assets\sortify.ico --add-data "assets;assets" --name Sortify-GUI run_gui.py
```

CLI version:

```bash
pyinstaller --onefile --icon=assets\sortify.ico --name Sortify run_sortify.py
```

---

## ✅ Run Tests

Run the test suite:

```bash
pytest -v
```

---

## 🛠 Technologies

* Python 3.13
* pathlib
* shutil
* argparse
* tkinter
* threading
* logging
* pytest
* PyInstaller
* Git

---

## 📄 License

MIT License
