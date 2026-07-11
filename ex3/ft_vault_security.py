def secure_archive(
    file_name: str, op: str = "r", write_str: str = ""
) -> tuple[bool, str]:
    try:
        if op == "r":
            with open(file_name, op) as file:
                return (True, file.read())
        if op == "w":
            with open(file_name, op) as file:
                file.write(write_str)
                return (True, write_str)
        return (False, f"Invalid operation: '{op}'")
    except OSError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive(
        "new_file.txt", "w", "Content successfully written to file"
    ))
