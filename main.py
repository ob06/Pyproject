import tkinter as tk
from tkinter import filedialog
import img2pdf
import os

def convert_to_pdf():
    filepath = entry.get()
    output_directory = output_entry.get()

    if not filepath:
        status_label.config(text="Please select a file or directory")
        return

    if os.path.isdir(filepath):
        output_filename = os.path.join(output_directory, "output.pdf")
        with open(output_filename, "wb") as f:
            imgs = []
            for fname in os.listdir(filepath):
                if not fname.lower().endswith((".jpg", ".jpeg")):
                    continue
                path = os.path.join(filepath, fname)
                if os.path.isdir(path):
                    continue
                imgs.append(path)
            f.write(img2pdf.convert(imgs))
        status_label.config(text=f"PDF generated: {output_filename}")
    elif os.path.isfile(filepath):
        if filepath.lower().endswith((".jpg", ".jpeg")):
            output_filename = os.path.join(output_directory, "output.pdf")
            with open(output_filename, "wb") as f:
                f.write(img2pdf.convert(filepath))
            status_label.config(text=f"PDF generated: {output_filename}")
        else:
            status_label.config(text="Please select a JPG file")
    else:
        status_label.config(text="File or directory does not exist")

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def choose_output_directory():
    output_dir = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_dir)

root = tk.Tk()
root.title("Image to PDF Happy 2024!")

icon_file = "xmas_christmas_tree_emoji_icon_260217.ico"
if os.path.exists("xmas_christmas_tree_emoji_icon_260217.ico"):
    root.iconbitmap("xmas_christmas_tree_emoji_icon_260217.ico")

label = tk.Label(root, text="Select an image file or directory:")
label.pack()

entry = tk.Entry(root, width=100)
entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

output_label = tk.Label(root, text="Choose output directory:")
output_label.pack()

output_entry = tk.Entry(root, width=50)
output_entry.pack()

output_button = tk.Button(root, text="Choose", command=choose_output_directory)
output_button.pack()

convert_button = tk.Button(root, text="Convert to PDF", command=convert_to_pdf)
convert_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
