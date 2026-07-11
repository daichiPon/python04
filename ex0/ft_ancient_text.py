import sys
from typing import IO

def ft_one_arg(argv: list[str]) -> None:
    print(f"Usage: {argv} <file>")

def ft_open_file(arg: str) -> IO:
        try:
            io = open(arg,"r")
            contant = io.read()
            io.close()
            return contant
        except:
             print(f"Error opening file {arg}: [Errno 2] No such file or directory: {arg}")


if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        ft_one_arg(argv)
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file {argv[0]}")
        contant = ft_open_file(argv[1])
        if contant:
            print("---")
            print(f"{contant}")
            print("---")
            print(f"File {argv[1]} closed.")
