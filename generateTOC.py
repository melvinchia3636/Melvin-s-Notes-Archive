import os

EXCLUDED = ["readme.md", "generateTOC.py", ".DS_Store",
            ".obsidian", ".git", ".gitignore", "LICENSE", "README.md", ".vscode"]
EXCLUDED_EXTENSIONS = ["jpg", "png", "jpeg",
                       "gif", "svg", "aux", "fls", "log", "toc", "xdv", "gz", "synctex.gz(busy)", "fdb_latexmk"]


def listdir(stream, folder, indent=0):
    for item in sorted(os.listdir(folder)):
        if item not in EXCLUDED:
            if os.path.isdir(os.path.join(folder, item)):
                stream.write(
                    '{}\n<details>\n<summary>{}</summary>\n\n'.format("<dl><dd>"*indent, item))
                listdir(stream, os.path.join(folder, item), indent + 1)
                stream.write(
                    "\n</details>\n{}\n{}\n".format("</dd></dl>"*indent, "<hr></hr>" if indent == 0 else ""))
            else:
                if item.split(".")[-1] not in EXCLUDED_EXTENSIONS and not item.startswith("."):
                    stream.write("- [{}](<{}>)\n".format(item,
                                                         os.path.join(folder, item)))


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    listdir(file, ".")
