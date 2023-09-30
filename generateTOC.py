import os


def listdir(stream, folder, indent=""):
    for item in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, item)):
            stream.write('{}<details>\n{}<summary>{}</summary>\n\n'.format(
                         indent, indent, item))
            listdir(stream, os.path.join(folder, item), indent + "  ")
            stream.write("\n{}</details>\n\n".format(indent))
        else:
            if folder != "readme.md":
                stream.write("{}- [{}](<{}>)\n".format(indent, item,
                             os.path.join(folder, item)))


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    listdir(file, ".")
