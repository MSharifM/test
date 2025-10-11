# save as syscall_examples.py
import os
import sys

def example_write():
    # 1 = stdout
    os.write(1, b"hello from os.write()\n")

def meta_data():
    info = os.stat("t.py")
    print("size:", info.st_size, "bytes")

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 syscall_examples.py [write|file|forkexec|metadata]")
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
    else:
        print("unknown")
