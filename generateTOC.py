import os


def listdir(stream, folder):
    for item in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, item)):
            stream.write('<details>\n<summary>{}</summary>\n\n'.format(item))
            listdir(stream, os.path.join(folder, item))
            stream.write("\n</details>\n\n")
        else:
            if folder != "readme.md":
                stream.write("- [{}](<{}>)\n".format(item,
                             os.path.join(folder, item)))


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    listdir(file, ".")
