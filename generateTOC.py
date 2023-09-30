import os


def listdir(stream, folder, indent=0):
    for item in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, item)):
            stream.write(
                '<div style="margin-left:{}em">\n<details>\n<summary>{}</summary>\n\n'.format(indent, item))
            listdir(stream, os.path.join(folder, item), indent + 1)
            stream.write("\n</details>\n</div>\n\n")
        else:
            if folder != "readme.md":
                stream.write("- [{}](<{}>)\n".format(item,
                             os.path.join(folder, item)))


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    listdir(file, ".")
