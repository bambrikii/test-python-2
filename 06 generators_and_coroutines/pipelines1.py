def cat(file):
    for line in open(file):
        yield line


def grep(lines, search):
    for line in lines:
        if search in line:
            yield line


def replace(lines, search, replace):
    for line in lines:
        yield line.replace(search, replace)


for line in replace(replace(grep(cat("pipelines1.py"), "for"), "line", "lll"), "\n", "new-line"):
    print(line)
