import sys
from typing import IO


def ft_one_arg(argv: list[str]) -> None:
    print(f"Usage: {argv[0]} <file>")


def ft_open_file(arg: str) -> str | None:
    try:
        io: IO = open(arg, "r")
        file_str = io.read()
        io.close()
        return file_str
    except OSError as e:
        print(f"Error opening file '{arg}': {e}")
        return None


if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        ft_one_arg(argv)
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{argv[1]}'")
        file_str = ft_open_file(argv[1])
        if file_str is not None:
            print("---")
            print(file_str)
            print("---")
            print(f"File '{argv[1]}' closed.")
