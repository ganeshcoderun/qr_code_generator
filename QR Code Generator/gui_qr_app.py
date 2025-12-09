import qrcode
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def generate_qr():
    data = entry.get()

    if not data:
        messagebox.showerror("Error", "Please enter text or URL!")
        return

    try:
        qr = qrcode.make(data)
        filename = f"qr_gui_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        qr.save(filename)

        messagebox.showinfo("Success", f"QR Saved as {filename}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Window
root = Tk()
root.title("QR Code Generator")
root.geometry("400x250")
root.config(bg="#222")

Label(root, text="Enter Text or URL", font=("Arial", 14), bg="#222", fg="white").pack(pady=10)

entry = Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

Button(root, text="Generate QR", font=("Arial", 14), command=generate_qr,
       bg="green", fg="white", width=15).pack(pady=20)

root.mainloop()
