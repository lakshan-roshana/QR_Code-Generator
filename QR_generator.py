import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr():
    data = entry.get().strip()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some text or URL.")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Ask user where to save
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save QR Code as")
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved successfully at:\n{file_path}")

# Setup GUI window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")
root.resizable(False, False)

# Label
tk.Label(root, text="Enter Text or URL:", font=("Arial", 12)).pack(pady=10)

# Entry field
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Generate button
tk.Button(root, text="Generate QR Code", command=generate_qr, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)

# Run the application
root.mainloop()
