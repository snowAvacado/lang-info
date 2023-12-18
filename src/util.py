from pathlib import Path
import subprocess

#function to remove in temp folder
def rmdir(dir_path: Path):
    result = subprocess.run(["rm","-r","-f", dir_path], capture_output=True, text=True)
    if len(result.stderr):
        raise "cannot delete previous dir"
    

