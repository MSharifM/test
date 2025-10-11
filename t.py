# save as syscall_examples.py
import os
import sys
import time

def example_write():
    # 1 = stdout
    os.write(1, b"hello from os.write()\n")

def meta_data():
    info = os.stat("test.txt")
    print("size:", info.st_size, "bytes")
    print("last change:", time.ctime(info.st_mtime))
    print("last access:", time.ctime(info.st_atime))
    print("device ID:", info.st_dev)

def example_create_file():
    fd = os.open("testfile.txt", os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o644)
    os.write(fd, b"This was written by os.open/os.write/os.close\n")
    os.close(fd)
    print("wrote testfile.txt")

def example_fork_exec():
    print("befor fork:")
    pid = os.fork()
    if pid == 0:
        print(f"i am child: {os.getpid()}")
    else:
        print(f"i am parent: {os.getpid()}")

def read_file():
    fd = os.open("test.txt", os.O_RDONLY)  # → معادل open()
    data = os.read(fd, 1000)                # → معادل read()
    print(data.decode())

    os.close(fd)                           # → معادل close()

def read_only():
    try:
        os.chmod("test.txt", 0o444)   # معادل chmod 444
        print("Success")
    except:
        print("Unsuccess")

def unread_only():
    try:
        mode = os.stat("test.txt").st_mode
        os.chmod("test.txt", mode | 0o200) 
        print("Success")
    except:
        print("Unsuccess")

def delete_file():
    try:
        os.remove("testfile.txt") 
        print("Succcess")
    except:
        print("Failed")

if __name__ == "__main__":
    option = 0
    while(option != 9):
        print("\n*****************************")
        print("[1] Write a sentence")
        print("[2] Create new file")
        print("[3] Fork")
        print("[4] File information")
        print("[5] Read a file")
        print("[6] ReadOnly permission")
        print("[7] Remove RO permission")
        print("[8] Delete file")
        print("[9] Exit\n")
        option = int(input("Choose an option:"))
        print()

        if(option == 1):
            example_write()
        elif option == 2:
            example_create_file()
        elif option == 3:
            example_fork_exec()
        elif option == 4:
            meta_data()
        elif option == 5:
            read_file()
        elif option == 6:
            read_only()
        elif option == 7:
            unread_only()
        elif option == 8:
            delete_file()
        else:
            pass
            
