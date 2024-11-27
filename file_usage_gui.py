import os
from tkinter import Tk, Label, Button, filedialog, ttk

# Function to calculate folder size and list files
def calculate_folder_size(folder_path):
    total_size = 0
    file_list = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                total_size += size
                file_list.append((file_path, size / (1024 * 1024 * 1024)))  # Convert size to GB
            except OSError as e:
                print(f"Error accessing {file_path}: {e}")

    return total_size / (1024 * 1024 * 1024), file_list  # Total size in GB

# Function to browse and calculate folder size
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        total_size, file_list = calculate_folder_size(folder_path)
        display_results(total_size, file_list)

# Function to display results in the GUI
def display_results(total_size, file_list):
    for item in tree.get_children():
        tree.delete(item)

    for file_path, size in file_list:
        tree.insert("", "end", values=(file_path, f"{size:.2f} GB"))

    total_size_label.config(text=f"Total Folder Size: {total_size:.2f} GB")

# Create GUI
root = Tk()
root.title("Folder File Usage")

Label(root, text="Select a folder to analyze its file usage:").pack(pady=10)
Button(root, text="Browse Folder", command=browse_folder).pack(pady=5)

tree = ttk.Treeview(root, columns=("File Path", "Size (GB)"), show="headings")
tree.heading("File Path", text="File Path")
tree.heading("Size (GB)", text="Size (GB)")
tree.column("File Path", anchor="w", width=400)
tree.column("Size (GB)", anchor="center", width=100)
tree.pack(padx=10, pady=10, fill="both", expand=True)

total_size_label = Label(root, text="Total Folder Size: 0.00 GB")
total_size_label.pack(pady=10)

root.geometry("600x400")
root.mainloop()
