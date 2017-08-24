from modules.catalog_parser import catalogParser
from modules.get_poem import getPoem

def main():
    filepath = "catalog.txt"
    catalog = catalogParser(filepath)
    poetryPath = "poetry.md"
    with open(poetryPath, 'w', encoding="utf8") as f:
        f.write("# Poetry\n")
        for poem in catalog:
            poemInfo = getPoem(poem)
            f.write(("## %s\n**%s**\n> %s\n\n%s\n")%(poemInfo["title"], poemInfo["author"], poemInfo["content"], poemInfo["comment"]))

if __name__ == "__main__":
    main()