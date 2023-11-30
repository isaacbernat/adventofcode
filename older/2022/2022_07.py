from pprint import pprint
from collections import defaultdict

# PART 1
def read_input():
    with open("2022_07.input") as f:
        files, all_dirs, current_path = {}, set("/"), "/"
        for l in f.readlines():
            line = l.strip().split(" ")
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "/":
                        current_path = "/"
                    elif line[2] == "..":
                        current_path = "/".join(current_path.split("/")[:-1])
                    else:  # move to a dir
                        current_path += f"/{line[2]}"
            elif line[0] == "dir":
                all_dirs.add(f"{current_path}/{line[1]}")
            else:  # it's a file
                files[f"{current_path}/{line[1]}"] = int(line[0])
        return files, all_dirs


def size_dirs(files, all_dirs):
    dirs = defaultdict(int)
    for k, v in files.items():
        for d in all_dirs:
            if k.startswith(d):
                dirs[d] += v
    # pprint(dirs)
    # pprint(all_dirs)
    return dirs


files, all_dirs = read_input()
# pprint(files)
dirs = size_dirs(files, all_dirs)
total = sum([v for v in dirs.values() if v <= 100000])
print(total)

# WIP (You guessed 1963230.) too low...
