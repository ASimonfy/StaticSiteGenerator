import argparse
from copy_static import copy_static
from generate_pages_recursive import generate_pages_recursive

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-path",
        default="./",
        help="Base path for generated site (e.g. GitHub Pages URL)"
    )

    args = parser.parse_args()

    copy_static()
    generate_pages_recursive(
        args.base_path,
        "./content",
        "./template.html",
        "./docs"
    )

if __name__ == "__main__":
    main()