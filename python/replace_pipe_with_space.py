import sys

def replace_pipe_with_space(text):
    return text.replace("|", " ")

def main():
    # Check if input is being provided via stdin (e.g., piping using `|`)
    if not sys.stdin.isatty():
        for line in sys.stdin:
            print(replace_pipe_with_space(line), end="")
    # Check if a filename argument is provided
    elif len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            for line in file:
                print(replace_pipe_with_space(line), end="")
    else:
        print("Please provide an input file or pipe in the data.")

if __name__ == "__main__":
    main()
