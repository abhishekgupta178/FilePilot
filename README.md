📂 FILEPILOT — Smart File Organization System

An intelligent, Python-based file organizer that simplifies file management through automatic categorization and a user-friendly graphical interface.

FILEPILOT is a desktop application developed using Python and Tkinter to help users organize cluttered directories efficiently. It scans a selected folder, identifies files based on their extensions, and automatically moves them into appropriate category folders.

The project aims to reduce manual effort, improve file accessibility, and make digital file management simpler and more organized.

⸻

📌 Table of Contents

* Overview
* Problem Statement
* Objectives
* Key Features
* Technology Stack
* Project Architecture
* How It Works
* Project Structure
* Installation and Setup
* Usage
* File Categories
* Advantages
* Future Enhancements
* Author

⸻

🚀 Overview

Managing a large number of files manually can be time-consuming, especially when documents, images, videos, audio files, and programming files are stored together in a single directory.

FILEPILOT provides a simple solution by automating the file organization process. Users can select a directory, scan its contents, review the discovered files, and organize them into category-specific folders.

The application uses Python’s built-in file-handling capabilities and a graphical interface built with Tkinter.

❗ Problem Statement

As the number of digital files increases, maintaining an organized folder structure becomes difficult. Manually sorting files consumes time, reduces productivity, and can make important documents harder to locate.

Existing manual workflows require users to repeatedly identify file types and move them into appropriate folders.

FILEPILOT addresses this problem by automating file categorization and organization through a simple desktop application.

🎯 Objectives

* Automate repetitive file organization tasks.
* Categorize files according to their extensions.
* Provide an easy-to-use graphical interface.
* Reduce manual effort when managing directories.
* Prevent existing files from being overwritten during organization.
* Improve the accessibility and structure of digital files.

✨ Key Features

1. Graphical User Interface

A desktop interface built with Tkinter allows users to select folders and operate the application without using command-line instructions.

2. Folder Selection

Users can choose the directory they want to organize through a folder selection dialog.

3. File Scanning

The application scans the selected directory and identifies its files before making changes.

4. Automatic Categorization

Files are classified using their extensions. For example, PDF files are placed in Documents, JPG files in Images, and Python files in Code.

5. Automatic Folder Creation

The application creates category folders when needed, allowing files to be grouped systematically.

6. Duplicate Filename Protection

If a destination already contains a file with the same name, the organizer generates an alternative filename instead of overwriting the existing file.

7. Activity Logging

The interface displays file names and organization results so users can review what happened during the operation.

8. Error Handling

The application handles common file-operation errors and reports failures instead of silently ignoring them.

9. Dark Interface

A dark-themed interface provides a clean and modern appearance.

🛠️ Technology Stack

Technology	Purpose
Python 3	Core programming language
Tkinter	Graphical user interface
pathlib	File and directory path handling
os	Operating-system and file-related operations
shutil	Moving files between directories
Git and GitHub	Version control and source code hosting

The application uses Python’s standard library for its core functionality. Tkinter may need to be installed separately on some Linux systems.

🏗️ Project Architecture

FILEPILOT uses a modular architecture in which different files handle separate responsibilities.

Module	Responsibility
main.py	Initializes and launches the application
gui.py	Manages the graphical interface and user interactions
file_scanner.py	Scans the selected directory and returns files
category_engine.py	Maps file extensions to categories
file_organizer.py	Creates destination folders and moves files
README.md	Documents the project and setup instructions

This modular structure improves code readability, maintainability, and the ability to extend the application in the future.

⚙️ How It Works

The application follows a simple sequence:

1. Launch: The user starts FILEPILOT.
2. Select: The user selects a directory through the graphical interface.
3. Scan: The scanner identifies files in the selected directory.
4. Categorize: The category engine determines the appropriate category for each file.
5. Organize: The organizer creates destination folders and moves files into them.
6. Handle duplicates: Existing filenames are checked to avoid overwriting files.
7. Display results: The interface displays the outcome of the organization process.

Workflow Diagram

       Start Application
               |
               v
         Select Folder
               |
               v
          Scan Files
               |
               v
      Identify Extensions
               |
               v
      Determine Categories
               |
               v
       Create Destination
            Folders
               |
               v
          Move Files
               |
               v
       Display Results
               |
               v
              End

📁 Project Structure

FilePilot/
│
├── main.py
├── gui.py
├── file_scanner.py
├── category_engine.py
├── file_organizer.py
└── README.md

Each Python module has a clearly defined responsibility, helping separate the user interface, scanning logic, categorization rules, and file operations.

💻 Installation and Setup

Prerequisites

* Python 3.10 or later recommended
* Ubuntu/Linux, Windows, or another compatible desktop operating system
* Tkinter installed and available in your Python environment

Step 1: Clone the Repository

git clone https://github.com/abhishekgupta178/FilePilot.git
cd FilePilot

Step 2: Verify Python

On Ubuntu/Linux:

python3 --version

Step 3: Install Tkinter if Required

On Ubuntu/Linux:

sudo apt update
sudo apt install python3-tk

Step 4: Run the Application

python3 main.py

The graphical interface should open, allowing you to select and organize a folder.

🖱️ Usage

1. Launch FILEPILOT.
2. Click Select Folder.
3. Choose the directory you want to organize.
4. Click Scan Files to display the files found.
5. Review the list of files.
6. Click Organize Files.
7. Confirm the operation.
8. Review the results in the activity area.

Important: File organization moves files from their original locations. Always test the application on a temporary folder containing copies of your files before organizing important data.

🗂️ File Categories

FILEPILOT supports categories based on the configured file extensions.

Category	Example extensions
Documents	.pdf, .docx, .txt, .xlsx
Images	.jpg, .png, .gif, .svg
Videos	.mp4, .mkv, .avi, .mov
Audio	.mp3, .wav, .flac, .ogg
Archives	.zip, .rar, .7z, .tar
Code	.py, .c, .cpp, .java, .js
Applications	.exe, .deb, .apk, .appimage
Others	File extensions not covered by other categories

The category mapping can be extended by adding more file extensions to the categorization module.

🌟 Advantages

* Saves time by automating repetitive file management.
* Reduces manual effort and improves folder organization.
* Provides a graphical alternative to command-line file operations.
* Uses a modular and maintainable code structure.
* Helps prevent accidental overwriting of destination files.
* Can be extended with additional categories and features.

🔮 Future Enhancements

The following features could be added in future versions:

* Undo functionality: Restore files to their original locations after an organization operation.
* Preview mode: Show the proposed file movements before executing them.
* Advanced search: Search files by name, extension, or category.
* Custom categories: Allow users to define their own categorization rules.
* Duplicate detection: Identify files with identical content using file hashes.
* Activity history: Maintain a record of previous organization operations.
* Background processing: Keep the interface responsive while processing large directories.
* Scheduling: Automatically organize selected folders at predefined times.
* File statistics: Display the number of files organized in each category.

These are proposed enhancements and are not necessarily implemented in the current version.

🔐 Safety Considerations

FILEPILOT moves files within the selected directory and may create new folders during organization.

Users should:

* Review the selected directory before proceeding.
* Test the application with sample files first.
* Maintain backups of important documents.
* Avoid selecting system directories or folders containing files that must not be moved.

👨‍💻 Author

Abhishek Gupta

B.Tech — Computer Science and Engineering

SRM Institute of Science and Technology

⸻

📄 License

This project is intended for educational and personal development purposes. A formal open-source license can be added to specify how others may use, modify, and distribute the project.

⸻

⭐ If you find this project useful, consider starring the repository!

FILEPILOT — Organize Smarter. Work Better.
