import os


def listdir(folder, level=0, files=[]):
    for file in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file)):
            files.append([os.path.join(folder, file), level])
            listdir(os.path.join(folder, file), level + 1, files)
        else:
            files.append([os.path.join(folder, file), level])
    return files


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    for folder in os.listdir("."):
        if os.path.isdir(folder):
            file.write('<details>\n<summary>{}</summary>\n'.format(folder))
            file.write('\n'.join(["{}* [{}]({})".format("  " * file[1], file[0], file[0])
                       for file in listdir(folder)]))
            file.write("\n</details>\n")
