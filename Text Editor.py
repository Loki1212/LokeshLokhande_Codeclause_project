import io
# Read a file
def read_file(filename):
    with io.open(filename, "r", encoding="utf-8") as file:
        return file.read()


# Write to a file
def write_file(filename, content):
    with io.open(filename, "w", encoding="utf-8") as file:
        file.write(content)


# User interface
def main():
    while True:
        action = input("Enter a command (read, write, or quit): ")

        if action == "read":
            filename = input("Enter a file name: ")
            content = read_file(filename)
            print(content)
        elif action == "write":
            filename = input("Enter a file name: ")
            content = input("Enter text: ")
            write_file(filename, content)
            print("File saved.")
        elif action == "quit":
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
