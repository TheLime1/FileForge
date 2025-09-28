import os
import random
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
from pathlib import Path


class FileForgeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FileForge - File Generator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Configure style
        style = ttk.Style()
        style.theme_use('clam')

        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Title
        title_label = ttk.Label(
            main_frame, text="FileForge", font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # File name input
        ttk.Label(main_frame, text="File Name:", font=("Arial", 11)
                  ).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.filename_var = tk.StringVar(value="file")
        self.filename_entry = ttk.Entry(
            main_frame, textvariable=self.filename_var, font=("Arial", 11))
        self.filename_entry.grid(
            row=1, column=1, sticky="ew", pady=5, padx=(10, 0))

        # File extension input
        ttk.Label(main_frame, text="File Extension:", font=(
            "Arial", 11)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.extension_var = tk.StringVar(value="txt")
        self.extension_entry = ttk.Entry(
            main_frame, textvariable=self.extension_var, font=("Arial", 11))
        self.extension_entry.grid(
            row=2, column=1, sticky="ew", pady=5, padx=(10, 0))

        # Number of files
        ttk.Label(main_frame, text="Number of Files:", font=(
            "Arial", 11)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.num_files_var = tk.StringVar(value="1")
        self.num_files_entry = ttk.Entry(
            main_frame, textvariable=self.num_files_var, font=("Arial", 11))
        self.num_files_entry.grid(
            row=3, column=1, sticky="ew", pady=5, padx=(10, 0))

        # File type combo box
        ttk.Label(main_frame, text="File Type:", font=("Arial", 11)
                  ).grid(row=4, column=0, sticky=tk.W, pady=5)
        self.file_type_var = tk.StringVar(value="code")
        self.file_type_combo = ttk.Combobox(main_frame, textvariable=self.file_type_var,
                                            values=["code", "other"], state="readonly", font=("Arial", 11))
        self.file_type_combo.grid(
            row=4, column=1, sticky="ew", pady=5, padx=(10, 0))

        # Output directory selection
        ttk.Label(main_frame, text="Output Directory:", font=(
            "Arial", 11)).grid(row=5, column=0, sticky=tk.W, pady=5)
        directory_frame = ttk.Frame(main_frame)
        directory_frame.grid(row=5, column=1, sticky="ew",
                             pady=5, padx=(10, 0))

        self.output_dir_var = tk.StringVar(value="gen")
        self.output_dir_entry = ttk.Entry(
            directory_frame, textvariable=self.output_dir_var, font=("Arial", 10))
        self.output_dir_entry.grid(row=0, column=0, sticky="ew")

        self.browse_button = ttk.Button(
            directory_frame, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=1, padx=(5, 0))

        directory_frame.columnconfigure(0, weight=1)

        # Size range info
        self.size_info_label = ttk.Label(
            main_frame, text="Size: 1KB - 10KB", font=("Arial", 10), foreground="blue")
        self.size_info_label.grid(row=6, column=0, columnspan=2, pady=10)

        # Update size info when file type changes
        self.file_type_combo.bind(
            '<<ComboboxSelected>>', self.update_size_info)

        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=7, column=0, columnspan=2, sticky="ew", pady=10)

        # Generate button
        self.generate_button = ttk.Button(main_frame, text="Generate Files", command=self.generate_files,
                                          style="Accent.TButton")
        self.generate_button.grid(row=8, column=0, columnspan=2, pady=20)

        # Status label
        self.status_label = ttk.Label(
            main_frame, text="Ready to generate files", font=("Arial", 10))
        self.status_label.grid(row=9, column=0, columnspan=2, pady=5)

        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    def browse_directory(self):
        directory = filedialog.askdirectory(
            initialdir=self.output_dir_var.get())
        if directory:
            self.output_dir_var.set(directory)

    def update_size_info(self, event=None):
        if self.file_type_var.get() == "code":
            self.size_info_label.config(text="File Size Range: 1KB - 10KB")
        else:
            self.size_info_label.config(text="File Size Range: 1MB - 10MB")

    def generate_files(self):
        # Start generation in a separate thread to prevent GUI freezing
        thread = threading.Thread(target=self._generate_files_thread)
        thread.daemon = True
        thread.start()

    def _generate_files_thread(self):
        try:
            # Disable button and start progress
            self.root.after(
                0, lambda: self.generate_button.config(state='disabled'))
            self.root.after(0, lambda: self.progress.start())
            self.root.after(0, lambda: self.status_label.config(
                text="Generating files..."))

            # Validate inputs
            filename = self.filename_var.get().strip()
            extension = self.extension_var.get().strip()
            num_files_str = self.num_files_var.get().strip()
            file_type = self.file_type_var.get()
            output_dir = self.output_dir_var.get().strip()

            if not filename:
                raise ValueError("File name cannot be empty")
            if not extension:
                raise ValueError("File extension cannot be empty")
            if not num_files_str.isdigit() or int(num_files_str) <= 0:
                raise ValueError("Number of files must be a positive integer")

            num_files = int(num_files_str)

            # Generate files
            self.generate_random_files(
                filename, extension, num_files, file_type, output_dir)

            # Success message
            success_msg = f"Successfully generated {num_files} {extension} files in '{output_dir}' directory!"
            self.root.after(
                0, lambda: self.status_label.config(text=success_msg))
            self.root.after(0, lambda: messagebox.showinfo(
                "Success", success_msg))

        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.root.after(
                0, lambda: self.status_label.config(text=error_msg))
            self.root.after(
                0, lambda: messagebox.showerror("Error", error_msg))
        finally:
            # Re-enable button and stop progress
            self.root.after(
                0, lambda: self.generate_button.config(state='normal'))
            self.root.after(0, lambda: self.progress.stop())

    def clear_directory(self, directory):
        """Clear all files in the specified directory"""
        if os.path.exists(directory):
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    def generate_random_files(self, filename, extension, num_files, file_type, output_dir):
        """Generate random files based on the specified parameters"""
        # Define size ranges based on file type (new specifications)
        if file_type == "code":
            size_range = (1024, 10240)  # 1KB to 10KB
        else:  # other (zip, image, etc.)
            size_range = (1048576, 10485760)  # 1MB to 10MB

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Clear directory before generating new files
        self.clear_directory(output_dir)

        # Generate files
        for i in range(num_files):
            if num_files == 1:
                file_name = f"{filename}.{extension}"
            else:
                file_name = f"{filename}_{i+1}.{extension}"

            file_path = os.path.join(output_dir, file_name)
            file_size = random.randint(*size_range)

            with open(file_path, 'wb') as file:
                file.write(os.urandom(file_size))


def main():
    root = tk.Tk()
    app = FileForgeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
