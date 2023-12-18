import sys
import os
from pathlib import Path
from git import Repo
from util import rmdir
from  langext import lang_extension_dict

nroflines = dict()
problemfiles = list()
#function to count lines in directory
def count_lines_dir(dir_path: Path) -> int:
    total_lines_dir = 0
    total_lines_files = 0
    for file in dir_path.iterdir() :
        if file.is_symlink() or file.name.startswith("."):
            continue       
        elif file.is_dir() :
            total_lines_dir = total_lines_dir + count_lines_dir(file)
        else :
            fileExt = "." + file.name.split(".")[-1] 
            try:
                with open(file, 'r') as fp:
                    lines = len(fp.readlines()) 
                    if fileExt in nroflines:
                        nroflines[fileExt] += lines
                    else:
                        nroflines[fileExt] = lines
                    total_lines_files = total_lines_files + lines
            except:
                problemfiles.append(file)
    return total_lines_dir + total_lines_files

if __name__ == "__main__":
    if len(sys.argv) != 2 :
        print("usage: count_lines.py <repo_url>")
        exit()

    repo_url = sys.argv[1]
    testpath = Path(".").cwd().joinpath("count_lines")
    # check whether directory already exists
    if os.path.exists(testpath):
        print("count_lines.py: test Folder %s exists." % testpath)
        rmdir(testpath)
        os.mkdir(testpath)
    else:
        os.mkdir(testpath)
        print("count_lines.py: test Folder %s created" % testpath)
    try :
        Repo.clone_from(repo_url, testpath)
    except  :
        print("count_lines.py: problem with <repo_url> , failed")
        exit()
    total_lines = 0
    print("total: %d lines."%count_lines_dir(testpath))
    for key,value in nroflines.items():
        print(key,":",value)
    if len(problemfiles):
        print("Problems in counting lines in below files:")
        for file in problemfiles:
            print(file)
    print("success")


