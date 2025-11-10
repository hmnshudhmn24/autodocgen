def count_lines(file_path):
    with open(file_path) as f:
        return len(f.readlines())
