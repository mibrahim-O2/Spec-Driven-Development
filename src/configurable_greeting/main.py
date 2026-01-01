import argparse

def greet(name: str) -> str:
    """Generates a greeting string."""
    return f"Hello, {name}!"

def main():
    """Parses arguments and prints a greeting."""
    parser = argparse.ArgumentParser(description="Greets the user.")
    parser.add_argument("name", nargs="?", default="World", help="The name to greet.")
    args = parser.parse_args()
    print(greet(args.name))

if __name__ == "__main__":
    main()
