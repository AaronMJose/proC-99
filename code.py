import os
import shutil
path='\\Users\\sajan\\OneDrive\\Documents\\Python\\C-99'
print('before copying the file')
print(os.listdir(path))
source='\\Users\\sajan\\OneDrive\\Documents\\Python\\C-99\\abc.py'
destination='\\Users\\sajan\\OneDrive\\Documents\\Python\\C-99\\xyz.py'
dest= shutil.copy(source,destination)
print('after copying the file')
print(os.listdir(path))