import os

EXCLUDED = ["readme.md", "generateTOC.py", ".DS_Store",
            ".obsidian", ".git", ".gitignore", "LICENSE", "README.md", ".vscode"]
EXCLUDED_EXTENSIONS = ["jpg", "png", "jpeg",
                       "gif", "svg", "aux", "fls", "log", "toc", "xdv", ".gz", "synctex.gz(busy)", "fdb_latexmk"]


def listdir(stream, folder, indent=0):
    for item in sorted(os.listdir(folder)):
        if item not in EXCLUDED:
            if os.path.isdir(os.path.join(folder, item)):
                stream.write(
                    '<details>\n{}<summary>{}</summary>\n\n'.format("&nbsp;&nbsp;&nbsp;&nbsp;"*indent, item))
                listdir(stream, os.path.join(folder, item), indent + 1)
                stream.write(
                    "\n</details>\n\n")
            else:
                if item.split(".")[-1] not in EXCLUDED_EXTENSIONS and not item.startswith("."):
                    stream.write("{}- [{}](<{}>)\n".format("&nbsp;&nbsp;&nbsp;&nbsp;"*indent, item,
                                                           os.path.join(folder, item)))


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    listdir(file, ".")
