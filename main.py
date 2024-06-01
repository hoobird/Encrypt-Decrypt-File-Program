import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from encdec import genkey, writetofile, encryptfile, decryptfile

FONTLABEL = "Arial 14"

def selectfile(tkstrvar, ext=""):
    filename = filedialog.askopenfilename()
    if ext and not filename.endswith(f".{ext}"):
        messagebox.showerror("Error", f"Please select a {ext} file")
        return
    tkstrvar.set(filename)

def encryptfilebutton(filepath):
    filepath = filepath.get()
    filedir = "/".join(filepath.split("/")[:-1])
    filename = filepath.split("/")[-1]
    filename = filename.split(".")[0]

    try:
        key = genkey()
        with open(f"{filedir}/{filename}.key", "wb") as f:
            f.write(key)
    except Exception as e:
        messagebox.showerror("Error", f"Error generating key: {e}")
        return
    try:
        encryptfile(filepath, key)
    except Exception as e:
        messagebox.showerror("Error", f"Error encrypting file: {e}")
        return
    messagebox.showinfo("File Successfuly Encrypted", 
                        f"Key generated at: {filedir}/{filename}.key\nEncrypted file at: {filepath}.enc")

def decryptfilebutton(filepath, keypath):
    filepath = filepath.get()
    keypath = keypath.get()
    filename = filepath.split("/")[-1]
    fileext = filename.split(".")[-2]
    filename = ".".join(filename.split(".")[:-2])
    try:
        with open(keypath, "rb") as f:
            key = f.read()
        decryptfile(filepath, key)
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", "Error decrypting file")
        return
    messagebox.showinfo("File Successfully Decrypted", f"Decrypted file at: {filename}_dec.{fileext}")


def gui():
    root = tk.Tk()
    root.geometry("550x200")
    root.title("Encrypt/Decrypt your files")
    tabcontrol = ttk.Notebook(root)
    tabenc = ttk.Frame(tabcontrol)
    tabdec = ttk.Frame(tabcontrol)
    setupenctab(tabenc)
    setupdectab(tabdec)
    tabcontrol.add(tabenc, text="Encrypt")
    tabcontrol.add(tabdec, text="Decrypt")
    tabcontrol.pack(expand=1, fill="both")
    root.mainloop()

def setupenctab(tab):
    filepath = tk.StringVar()

    ttk.Label(tab, text="Select a file to encrypt", font=FONTLABEL).grid(row=0, column=0, padx = 30)
    ttk.Entry(tab, textvariable=filepath, width=60).grid(row=1, column=0, padx=20)
    ttk.Button(tab, text="Browse",command=lambda: selectfile(filepath)).grid(row=1, column=1, padx = 30)
    ttk.Button(tab, text="Encrypt", command=lambda: encryptfilebutton(filepath)).grid(row=2, column=0, padx = 30, pady = 10)

def setupdectab(tab):
    filepath = tk.StringVar()
    keypath = tk.StringVar()

    ttk.Label(tab, text="Select a file to decrypt", font=FONTLABEL).grid(row=0, column=0, padx = 30)
    ttk.Entry(tab, textvariable=filepath, width=60).grid(row=1, column=0, padx=20)
    ttk.Button(tab, text="Browse",command=lambda: selectfile(filepath, "enc")).grid(row=1, column=1, padx = 30)
    ttk.Label(tab, text="Select the key file", font=FONTLABEL).grid(row=2, column=0, padx = 30)
    ttk.Entry(tab, textvariable=keypath, width=60).grid(row=3, column=0)
    ttk.Button(tab, text="Browse",command=lambda: selectfile(keypath, "key")).grid(row=3, column=1, padx = 30)
    ttk.Button(tab, text="Decrypt", command=lambda: decryptfilebutton(filepath, keypath)).grid(row=4, column=0, padx = 30, pady = 10)


     


def main():
    gui()

if __name__ == "__main__":
    main()
