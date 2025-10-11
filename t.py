# save as syscall_examples.py
import os
import sys
import time

def example_write():
    # 1 = stdout
    os.write(1, b"hello from os.write()\n")

def meta_data():
    info = os.stat("t.py")
    print("size:", info.st_size, "bytes")
    print("last change:", time.ctime(info.st_mtime))
    print("last access:", info.st_atime, "bytes")
    print("device ID:", info.st_dev, "bytes")

def example_create_file():
    fd = os.open("testfile.txt", os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o644)
    os.write(fd, b"This was written by os.open/os.write/os.close\n")
    os.close(fd)
    print("wrote testfile.txt")

def example_fork_exec():
    pid = os.fork()
    if pid == 0:
        # child
        print("child: exec ls -l")
        os.execv("/bin/ls", ["/bin/ls", "-l"])
        # execv برنگردد اگر موفق باشه
    else:
        # parent
        pid, status = os.waitpid(pid, 0)
        print("parent: child exited, status:", status)

def read_file():
    fd = os.open("t.py", os.O_RDONLY)  # → معادل open()
    data = os.read(fd, 1000)                # → معادل read()
    print(data.decode())

    os.close(fd)                           # → معادل close()

def read_only():
    try:
        os.chmod("re.py", 0o444)   # معادل chmod 444
        print("Success")
    except:
        print("Unsuccess")

def unread_only():
    try:
        mode = os.stat("re.py").st_mode
        os.chmod("re.py", mode | 0o200) 
        print("Success")
    except:
        print("Unsuccess")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 syscall_examples.py [write|file|forkexec|metadata|read|change-per|un]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "write":
        example_write()
    elif cmd == "file":
        example_create_file()
    elif cmd == "forkexec":
        example_fork_exec()
    elif cmd == "metadata":
        meta_data()
    elif cmd == "read":
        read_file()
    elif cmd == "change-per":
        read_only()
    elif cmd == "un":
        unread_only()
    else:
        print("unknown")
