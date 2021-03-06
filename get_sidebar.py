import os
import re

TITLE = "* {}"
SUBTITLE = "    * [{}]({})"
TOC_TITLE = "\n### {}\n"
TOC_LIST = "* [{}]({})"
IGNORE_DIRS = [
    ".git",
    "old",
    "static",
]


class Generate():
    """
    Get _sidebar.md and README.md's TOC automatic,
    please input the directory you want to ignore in 'IGNORE_DIRS'
    """
    sidebar = open("_sidebar.md", "w")
    readme = open("README.md", "r+")

    def write(self, f, content):
        f.write(content + "\n")

    def main(self):
        pattern = r'[\s\S]*Table Of Contents'
        toc = re.search(pattern, self.readme.read()).group()
        self.readme.seek(0)
        self.write(self.readme, toc)
        self.write(self.sidebar, "* [Headline](README.md)")

        tree = os.walk("./", topdown=True)
        for root, dirs, files in tree:
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            if root == "./":
                continue
            title = root.split("./")[-1]
            self.write(self.readme, TOC_TITLE.format(title.capitalize()))
            self.write(self.sidebar, TITLE.format(title.capitalize()))
            for file in files:
                subtitle, path = file[:-3], f"{title}/{file}"
                self.write(self.readme, TOC_LIST.format(subtitle, path))
                self.write(self.sidebar, SUBTITLE.format(subtitle, path))
        self.sidebar.close()
        self.readme.close()


if __name__ == '__main__':
    hi = Generate()
    hi.main()
