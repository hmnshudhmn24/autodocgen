import argparse
from inference import generate_doc

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to Python file to document")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        code = f.read()
    print(generate_doc(code))
