from modules.catalog_parser import catalogParser
from modules.get_poem import getPoem

def main():
    filepath = "catalog.txt"
    catalog = catalogParser(filepath)
    poem = getPoem(catalog[0])
    print(poem)

if __name__ == "__main__":
    main()