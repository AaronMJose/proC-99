import os
import shutil
path='\\Users\\sajan\\OneDrive\\Documents\\Python\\C-99'
print('before moving the file')
print(os.listdir(path))
source='\\Users\\sajan\\OneDrive\\Documents\\Python\\C-99\\xyz.py'
destination='\\Users\\sajan\\OneDrive\\Documents\\Python\\C-99\\my folder'
dest= shutil.move(source,destination)
print('after moving the file')
print(os.listdir(path))