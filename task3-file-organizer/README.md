<div align="center">

# 📁 Automated File Organizer & Cleanup Utility

**Datheon Python Programming Internship: Task 3**

A Python automation script that cleans up cluttered directories by sorting files into categorized folders using Python OS libraries.

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/type-automation-orange)
![Status](https://img.shields.io/badge/status-complete-brightgreen)

</div>

---

## 🎯 Features

- **Automated Sorting:** Moves files into folders based on their extensions: Documents, Images, Videos, Archives, Code, and Others for unknown types.
- **Collision Handling:** If a file with the same name already exists in the destination, it is renamed (e.g., `report_1.pdf`) instead of being overwritten.
- **Error Handling:** Catches `PermissionError` and other exceptions, then continues with the remaining files.
- **Execution Summary:** Prints the total number of files relocated, renamed, and skipped due to errors.
- **Filesystem Operations:** Uses core OS libraries for safe and efficient directory navigation and file relocation.

## 🛠️ Technology Stack

| Category          | Details                  |
|-------------------|--------------------------|
| Language          | Python 3                 |
| Standard Libraries| `os`, `shutil`, `pathlib`|

## 📂 How Files Are Sorted

| Folder      | Examples of file types |
|-------------|------------------------|
| Documents   | PDF, DOCX, TXT         |
| Images      | JPG, PNG, GIF          |
| Videos      | MP4, MKV, AVI          |
| Archives    | ZIP, RAR, TAR          |
| Code        | PY, JS, HTML           |
| Others      | Any unknown extension  |

> Update the "Examples" column to match the extensions your `organizer.py` actually handles.

## 🚀 How to Run

1. **Navigate to the project directory**
   ```bash
   cd task3-file-organizer
   ```

2. **Run the automation script**
   ```bash
   python organizer.py
   ```

3. **Enter the path** of the directory you want to organize when prompted.

## 👩‍💻 Author

**Tahmina Khan Nipa**

- GitHub: [@TahminaKhanNipa10-Codes](https://github.com/TahminaKhanNipa10-Codes)
- Datheon Batch: 01

---

<div align="center">⭐ If you found this useful, consider giving it a star!</div>
