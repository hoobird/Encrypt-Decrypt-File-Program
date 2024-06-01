# cryptography library
from cryptography.fernet import Fernet

def genkey():
    key = Fernet.generate_key()
    return key

def writetofile(txt, filename, ext):
    with open(f"{filename}.{ext}", "wb") as file:
        file.write(txt)

def encryptfile(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        txt = file.read()
    enc = f.encrypt(txt)
    writetofile(enc, filepath, "enc")

def decryptfile(filepath, key):
    if not filepath.endswith(".enc"):
        print("File is not encrypted")
        return
    f = Fernet(key)
    with open(filepath, "rb") as file:
        txt = file.read()
    dec = f.decrypt(txt)
    filedir = "/".join(filepath.split("/")[:-1])
    filename = ".".join(filepath.split("/")[-1].split(".")[:-2])
    fileext = filepath.split("/")[-1].split(".")[-2]
    writetofile(dec, filedir+'/'+filename+"_dec", fileext)

def main():
    # key = genkey()
    # with open("erm.key", "wb") as f:
    #     f.write(key)
    # encryptfile("./test.txt", key)
    
    # with open("erm.key", "rb") as f:   
    #     key = f.read()
    # decryptfile("./test.txt.enc", key)
    pass


if __name__ == "__main__":
    main()
