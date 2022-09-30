import sys
from argparse import ArgumentParser

from loader import RUNTIME_ERRORS, load_from_yaml
from render import print_relationships

ap = ArgumentParser(
    prog="", description=""
)

ap.add_argument(
    "path",
    type=str,
    help="Path of the directory where the files are",
)


def main():
    args = ap.parse_args()
    if not args.path:
        ap.print_help()
        return 1
    tables = load_from_yaml(args.path)
    print_relationships(tables)
    if RUNTIME_ERRORS:
        print('\nErrors:')
        [print(i) for i in RUNTIME_ERRORS]


if __name__ == "__main__":
    sys.exit(main())
