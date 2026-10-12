
import tkinter as tk
from tkinter import filedialog, messagebox
from file_scanner import scan_files
from file_organizer import organize_files


class FilePilot:
    def __init__(self, root):
        self.root = root
        self.root.title("FILEPILOT | Smart File Organizer")
        self.root.geometry("720x520")
        self.root.configure(bg="#111827")
        self.folder = ""
        self.files = []

        tk.Label(
            root, text="FILEPILOT",
            font=("Arial", 25, "bold"),
            fg="#60A5FA", bg="#111827"
        ).pack(pady=15)

        tk.Label(
            root, text="Smart File Organization System",
            fg="white", bg="#111827"
        ).pack()

        tk.Button(
            root, text="Select Folder",
            command=self.select_folder,
            bg="#2563EB", fg="white",
            width=22
        ).pack(pady=12)

        self.path_label = tk.Label(
            root, text="No folder selected",
            fg="#D1D5DB", bg="#111827",
            wraplength=650
        )
        self.path_label.pack()

        tk.Button(
            root, text="Scan Files",
            command=self.scan,
            bg="#374151", fg="white",
            width=22
        ).pack(pady=8)

        tk.Button(
            root, text="Organize Files",
            command=self.organize,
            bg="#059669", fg="white",
            width=22
        ).pack(pady=8)

        self.output = tk.Text(
            root, height=13, width=78,
            bg="#1F2937", fg="#F9FAFB",
            insertbackground="white"
        )
        self.output.pack(padx=15, pady=12)

    def select_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.folder = folder
            self.path_label.config(text=folder)
            self.files = []
            self.output.delete("1.0", tk.END)

    def scan(self):
        if not self.folder:
            messagebox.showwarning(
                "Select Folder", "Please select a folder first."
            )
            return

        try:
            self.files = scan_files(self.folder)
            self.output.delete("1.0", tk.END)

            for file in self.files:
                self.output.insert(tk.END, file.name + "\n")

            self.output.insert(
                tk.END, f"\nTotal files found: {len(self.files)}\n"
            )
        except (OSError, ValueError) as error:
            messagebox.showerror("Scan Error", str(error))

    def organize(self):
        if not self.folder:
            messagebox.showwarning(
                "Select Folder", "Please select a folder first."
            )
            return

        if not self.files:
            messagebox.showwarning(
                "Scan First", "Scan the folder before organizing."
            )
            return

        if not messagebox.askyesno(
            "Confirm",
            f"Organize {len(self.files)} files in the selected folder?"
        ):
            return

        results = organize_files(self.folder, self.files)
        self.output.delete("1.0", tk.END)

        for result in results:
            self.output.insert(tk.END, result + "\n")

        self.files = []
        messagebox.showinfo("Complete", "File organization finished!")
