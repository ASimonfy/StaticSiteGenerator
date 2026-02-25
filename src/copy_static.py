import os
import shutil

source_dir = "./static"
target_dir = "./docs"

def copy_static():
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    
    copyFiles(source_dir, target_dir)

def copyFiles(source_path, target_path):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for file in os.listdir(source_path):
        file_path_source = os.path.join(source_path, file)
        file_path_target = os.path.join(target_path, file)

        is_dir = os.path.isdir(file_path_source)
        is_file = os.path.isfile(file_path_source)
        if (is_dir):
            os.mkdir(file_path_target)
            copyFiles(file_path_source, file_path_target)
        if (is_file):
            shutil.copy(file_path_source, file_path_target)