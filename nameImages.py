import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ImageRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Renamer")

        # Get all .png images in the current directory
        self.image_files = [f for f in os.listdir() if f.endswith(".png")]
        print(self.image_files)
        self.current_index = 0

        if not self.image_files:
            messagebox.showinfo("No Images", "No .png images found in the directory.")
            root.destroy()
            return

        # Create GUI elements
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.rename_image)  # Bind Enter key to rename

        self.next_button = tk.Button(root, text="Save", command=self.rename_image)
        self.next_button.pack(pady=5)

        self.show_image()

    def show_image(self):
        """Display the current image in the GUI."""
        if self.current_index < len(self.image_files):
            image_path = self.image_files[self.current_index]
            img = Image.open(image_path)
            img = img.resize((400, 100))  # Resize for display
            self.tk_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_image)
        else:
            messagebox.showinfo("Done", "All images have been renamed!")
            self.root.destroy()

    def rename_image(self, event=None):
        """Rename the displayed image based on user input."""
        new_name = self.entry.get().strip()
        if not new_name:
            messagebox.showwarning("Error", "Please enter a valid name!")
            return

        new_file = new_name + ".png"

        # Ensure the new filename is unique
        if os.path.exists(new_file):
            messagebox.showwarning("Error", "File name already exists!")
            return

        # Rename the file
        old_name = self.image_files[self.current_index]
        os.rename(old_name, new_file)

        # Update list and move to the next image
        self.image_files[self.current_index] = new_file
        self.current_index += 1
        self.entry.delete(0, tk.END)  # Clear input box
        self.show_image()

    def show_next_image(self):
        """Move to the next image without renaming."""
        self.current_index += 1
        self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageRenamerApp(root)
    root.mainloop()

    print("All images have been renamed!")