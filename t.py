argv = (ctypes.c_char_p * 3)()
    argv[0] = b"/bin/echo"
    argv[1] = b"hello-from-execve"
    argv[2] = None
    env = (ctypes.c_char_p * 1)()
    env[0] = None
    # This does not return if successful
    libc.execve(b"/bin/echo", argv, env)
    # If returns -> error
    print("execve failed, errno:", ctypes.get_errno())
