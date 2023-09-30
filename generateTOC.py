import os


def listdir(stream, folder, indent=0):
    for item in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, item)):
            stream.write(
                '<{}>\n<details>\n<summary>{}</summary>\n\n'.format(["dl", "dd"][indent % 2], item))
            listdir(stream, os.path.join(folder, item), indent + 1)
            stream.write(
                "\n</details>\n</{}>\n\n".format(["dl", "dd"][indent % 2]))
        else:
            if folder != "readme.md":
                stream.write("- [{}](<{}>)\n".format(item,
                             os.path.join(folder, item)))


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    listdir(file, ".")
