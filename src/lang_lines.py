import sys
import os
import time
import subprocess

from pathlib import Path
from git import Repo

from lang_extns import lang_extensions_map

#function to remove in temp folder
def rmdir(dir_path: Path):
    result = subprocess.run(["rm","-r","-f", dir_path], capture_output=True, text=True)
    if len(result.stderr):
        raise "cannot delete previous dir"

lang_lines_map = dict()
lang_files_map = dict()
failed_to_read_files = list()

#counts lines in directory recursively
def count_lines_dir(dir_path: Path) -> int:
    lines_in_dir = 0
    lines_in_files = 0
    for file in dir_path.iterdir() :
        if file.is_symlink() or file.name.startswith("."):
            continue       
        elif file.is_dir() :
            lines_in_dir = lines_in_dir + count_lines_dir(file)
        else :
            file_extn = "." + file.name.split(".")[-1]
            try:
                with open(file, 'r') as fp:
                    lines = len(fp.readlines()) 
                    if file_extn in lang_lines_map:
                        lang_lines_map[file_extn] += lines
                    else:
                        lang_lines_map[file_extn] = lines
                    lines_in_files = lines_in_files + lines
                    if file_extn in lang_files_map:
                        lang_files_map[file_extn] += 1
                    else:
                        lang_files_map[file_extn] = 1
            except:
                failed_to_read_files.append(file)
    return lines_in_dir + lines_in_files

if __name__ == "__main__":
    if len(sys.argv) != 2 :
        print("usage: lang_lines.py <repo_url>")
        exit()
    
    repo_url = sys.argv[1]
    temp_test_path = Path(".").cwd().joinpath("lang_lines")
    # check if directory exists, if exists remove and create new
    if os.path.exists(temp_test_path):
        print("lang_lines.py: test Folder %s already exists. deleting.." % temp_test_path)
        rmdir(temp_test_path)
        os.mkdir(temp_test_path)
    else:
        os.mkdir(temp_test_path)
    try :
        Repo.clone_from(repo_url, temp_test_path)
    except  :
        print("lang_lines.py: problem with <repo_url> , failed")
        exit()
    start_time = time.time()
    total_lines = count_lines_dir(temp_test_path)
    print("total: %d lines."%total_lines)
    for key,value in lang_lines_map.items():
        print(lang_files_map[key],key,":",value)
    if len(failed_to_read_files):
        for file in failed_to_read_files:
            file_extn = "." + file.name.split(".")[-1]
            if file_extn in lang_extensions_map.keys():
                print("Problems in counting lines in below file:")
                print(file.name)
    print("success, time elapsed : %f seconds"%(time.time()-start_time))
    rmdir(temp_test_path)