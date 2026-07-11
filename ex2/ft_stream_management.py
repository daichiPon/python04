import sys


def ft_one_arg(argv: list[str]) -> None:
    print(f"Usage: {argv[0]} <file>")


def ft_open_file(arg: str) -> str | None:
    try:
        io = open(arg, "r")
        file_str = io.read()
        io.close()
        return file_str
    except OSError as e:
        print(f"[STDERR] Error opening file '{arg}': {e}", file=sys.stderr)
        return None


def add_hash(file_str: str) -> None:
    new_str = file_str.replace("\n", "#\n")
    if not new_str.endswith("\n"):
        new_str += "#"
    print("Transform data:")
    print("---")
    print(new_str)
    print("---")
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    file_name = sys.stdin.readline().strip()
    if file_name:
        print(f"Saving data to '{file_name}'")
        try:
            new_file = open(file_name, "w")
            new_file.write(new_str)
            new_file.close()
            print(f"Data saved in file '{file_name}'.")
        except OSError as e:
            print(f"[STDERR] Error opening file '{file_name}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        ft_one_arg(argv)
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{argv[1]}'")
        file_str = ft_open_file(argv[1])
        if file_str is not None:
            print("---")
            print(file_str)
            print("---")
            print(f"File '{argv[1]}' closed.")
            add_hash(file_str)
