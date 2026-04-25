def count_loc(code):
    if not code:
        return 0
    return len([line for line in code.split("\n") if line.strip()])