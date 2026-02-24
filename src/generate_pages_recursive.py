import os

from generate_page import generate_page

def generate_pages_recursive(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    generate_pages(from_path, template_path, dest_path)

def generate_pages(from_path, template_path, dest_path):

    for file in os.listdir(from_path):
        file_path_source = os.path.join(from_path, file)

        is_dir = os.path.isdir(file_path_source)
        is_file = os.path.isfile(file_path_source)
        if is_dir:
            file_path_target = os.path.join(dest_path, file)
            if not os.path.exists(file_path_target):
                os.mkdir(file_path_target)
            generate_pages(file_path_source, template_path, file_path_target)
        if is_file and file.endswith(".md"):
            dest_filename = file[:-3] + ".html"
            file_path_target = os.path.join(dest_path, dest_filename)
            generate_page(file_path_source, template_path, file_path_target)