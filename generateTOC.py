import os

EXCLUDED = ["readme.md", "generateTOC.py", ".DS_Store",
            ".obsidian", ".git", ".gitignore", "LICENSE", "README.md"]
EXCLUDED_EXTENSIONS = ["jpg", "png", "jpeg", "gif", "svg"]


def listdir(stream, folder, indent=0):
    for item in sorted(os.listdir(folder)):
        if item not in EXCLUDED:
            if os.path.isdir(os.path.join(folder, item)):
                stream.write(
                    '<{}>\n<details>\n<summary>{}</summary>\n\n'.format(["dl", "dd"][indent % 2], item))
                listdir(stream, os.path.join(folder, item), indent + 1)
                stream.write(
                    "\n</details>\n</{}>\n\n".format(["dl", "dd"][indent % 2]))
            else:
                if item.split(".")[-1] not in EXCLUDED_EXTENSIONS and not item.startswith("."):
                    stream.write("- [{}](<{}>)\n".format(item,
                                                         os.path.join(folder, item)))


with open("readme.md", "w") as file:
    file.write("# Table of Contents\n")
    listdir(file, ".")
