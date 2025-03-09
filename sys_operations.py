import os
import sys
import platform
import socket
import multiprocessing as mp  # Import multiprocessing

# Lab 9 Question 3.a.a., 3.a.b.
# Machine Type and Processor Type
print(platform.machine())
print(platform.architecture())

# Lab 9 Question 3.a.c., 3.a.d.
# Set and Get socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

# Lab 9 Question 3.a.e.
# OS name
print(os.name)
print(platform.system())

# Lab 9 Question 3.a.f.
# Process ID - Unique to every run
print(os.getpid())

# Lab 9 Question 3.b.a.
# File Descriptors
# Open (or create) a file named fdpractice.txt
f_name = "fdpractice.txt"
# with open("fdpractice.txt ", "a+") as f:
#    print(f.readline())
#    f.write("Hello World")

# f1 = open(f_name, "r")
# print(f1)
# f1.close()

f = os.open(f_name, os.O_RDWR | os.O_CREAT) # Open (or create) a file
print(f)

f_obj = os.fdopen(f, "a+") # Convert file descriptor into a file object
print(f_obj)
f_obj.close()
print()

# Lab 9 Question 3.b.e.
# print("Before fork: ", os.getpid())
# p = os.fork()
# print("After fork: ", os.getpid())

# if p ==0:
#    print("Child Process")
#    print("Parent Process PID: ", os.getpid())
# else:
#    print("Parent Process")
#    os.wait()
#    print("Child Process PID: ", p)
# print("Last Line")



# Child process function (for Windows)
def child_process():
    print("Child Process")
    print(f"Child Process ID: {os.getpid()}")

    # Open file and move pointer to the beginning
    with open(f_name, "r") as f:
        f.seek(0)
        content = f.read(100)  # Read up to 100 bytes
        print("File Content in Child Process:", content)

    # Process exits automatically when function ends

# Windows: Using multiprocessing instead of os.fork()
if __name__ == "__main__":
    print("Before process creation:", os.getpid())

    context = mp.get_context('spawn')  # Use 'spawn' to create a new process
    p = context.Process(target=child_process)  # Create child process
    p.start()  # Start child process

    print("After process creation:", os.getpid())

    print("Parent Process")

    p.join()  # Wait for child to finish

    print(f"Child Process PID: {p.pid}")

    # Parent process closes the file
    with open(f_name, "a+") as parent_file:
        print("Parent process closing file.")

    print("Last Line")