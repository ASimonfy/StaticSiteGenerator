from copy_static import copy_static
from generate_pages_recursive import generate_pages_recursive

def main(*args, **kwargs):
    base_path = args[0] if len(args) > 0 else "./"
    copy_static(base_path)
    generate_pages_recursive(base_path, "./content", "./template.html", "./docs")

main()