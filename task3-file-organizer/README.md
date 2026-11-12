📁 Automated File Organizer & Cleanup Utility

Datheon Python Programming Internship - Task 3

A Python automation script that cleans up cluttered directories by sorting files into categorized folders using Python OS libraries.

🎯 Project Features
Automated Sorting: Categorizes and moves files into specific folders based on their file extensions (Documents, Images, Videos, Archives, Code, and Others for unknown types).
Collision Handling: If a file with the same name already exists in the destination, the file is renamed (e.g., report_1.pdf) instead of being overwritten.
Error Handling: Catches PermissionError and other exceptions, and continues with the remaining files.
Execution Summary: Prints total files relocated, renamed, and skipped due to errors.
Filesystem Operations: Uses core OS libraries for safe and efficient directory navigation and file relocation.
🛠️ Technology Stack
Language: Python 3
Standard Libraries: os, shutil, pathlib
🚀 How to Run
Navigate to the project directory:
cd task3-file-organizer
Run the automation script:
python organizer.py
Enter the path of the directory you want to organize when prompted.
👨‍💻 Author

Tahmina Khan Nipa

GitHub: @TahminaKhanNipa10-Codes
Datheon Batch: 01