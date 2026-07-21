# 📂 Sortify

A Python CLI application that automatically organizes files into categorized folders based on their file extensions.

## ✨ Features

- Organize files by type
- Supports:
  - Images
  - Videos
  - Music
  - PDFs
  - Archives
  - Programs
- Dry-run mode
- Logging
- Command-line interface (CLI)
- Automated tests with pytest

## 📁 Project Structure

```
# Sortify/
│
├── main.py
├── organizer.py
├── config.py
├── logger_config.py
├── tests/
├── requirements.txt
└── README.md
```

## 🚀 Installation

```bash
git clone <repository-url>

cd download-organizer

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## ▶️ Usage

Organize a folder:

```bash
python main.py --folder "C:\Users\YourName\Downloads"
```

Preview changes without moving files:

```bash
python main.py --folder "C:\Users\YourName\Downloads" --dry-run
```

## ✅ Run Tests

```bash
pytest -v
```

## 🛠 Technologies

- Python 3
- pathlib
- shutil
- argparse
- logging
- pytest

## 📄 License

MIT