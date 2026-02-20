import os
from config import LARGE_FILE_SIZE_MB
def check_large_files(path="."):
    large_files=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            filepath=os.path.join(root,file)
            try:
                if os.path.getsize(filepath)>LARGE_FILE_SIZE_MB*1024*1024:
                    large_files.append(file)
            except:
                pass
    return large_files
