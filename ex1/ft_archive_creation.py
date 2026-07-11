import sys
from typing import IO

def ft_one_arg(argv: list[str]) -> None:
    print(f"Usage: {argv} <file>")

def ft_open_file(arg: str) -> IO:
        try:
            io = open(arg,"r")            
            file_str = io.read()
            io.close()
            return file_str
        except:
             print(f"Error opening file {arg}: [Errno 2] No such file or directory: {arg}")


def add_hash(file_str:str) -> None:
    new_str = file_str.replace("\n", "#\n")
    if not new_str.endswith("\n"):
        new_str += "#"
    print("---")
    print(new_str)
    print("---")
    file_name = input("Enter new file name (or empty):")
    if file_name:
         print(f"Saving data to {file_name}")
         new_file = open(file_name,"w")
         new_file.write(new_str)
         print(f"Data saved in file {file_name}.")
    else:
        print("Not saving data.")

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        ft_one_arg(argv)
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file {argv[0]}")
        file_str = ft_open_file(argv[1])
        if file_str:
            print("---")
            print(f"{file_str}")
            print("---")
            print(f"File {argv[1]} closed.")
            add_hash(file_str)