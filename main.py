__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
# from importlib.metadata import files
import os
import zipfile
from pathlib import Path


# current_path = os.getcwd()
# print(current_path)
files_path = Path(os.path.join(os.getcwd(), 'files')).absolute()
print(files_path)
cache_path = Path(os.path.join(files_path, 'cache')).absolute()
print(cache_path)
abs_path = Path(cache_path).absolute()
print(abs_path)
text_files = []


def clean_cache():
    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
    else:
        for file_name in os.listdir(cache_path):
            file = os.path.join(cache_path, file_name)
            # print(os.path.isfile(file))
            if os.path.isfile(file):
                os.remove(file)
        return


def cache_zip(zip_file_path, cache_dir_path):

    # test= os.path.abspath('data.zip')
    test = Path(os.path.join(zip_file_path, 'data.zip')).absolute()
    print(test)

    for _ in os.listdir(zip_file_path):
        if os.path.isfile(test):
            with zipfile.ZipFile(test, 'r') as zip_ref:
                zip_ref.extractall(cache_dir_path)
        return


def cached_files():
    for file_name in os.listdir(cache_path):
        if os.path.isfile(os.path.join(cache_path, file_name)):
            text_files.append(file_name)
    # print(text_files)
    return text_files


def find_password(files):
    index = 0
    for file_name in files:
        with open(os.path.join(abs_path, file_name), "r"):
            file = open(os.path.join(abs_path, file_name), "r")
        for line in file:
            index += 1
            if 'password' in line:
                password = line.split(":")
                file.close()
                print(str(password[1]).strip())
                return str(password[1]).strip()


clean_cache
cache_zip(files_path, cache_path)
cached_files()
find_password(text_files)
