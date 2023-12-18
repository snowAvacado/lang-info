from pathlib import Path
import subprocess
import os
#function to remove in directory
def rmdir(dir_path: Path):
    result = subprocess.run(["rm","-r","-f", dir_path], capture_output=True, text=True)
    if len(result.stderr):
        raise "cannot delete previous dir"
       
def rm_dir(dir_path: Path):
    for file in dir_path.iterdir() :
        if file.is_dir() :
            rm_dir(file)
        elif file.is_symlink() :
             continue
        else :
            os.remove(file)
    os.rmdir(dir_path)    

