#批量命名文件夹下的文件
import os
path = 'D:/python_project/filelist/'
files = os.listdir(path)
for file in files:
    old_name = path + file
    new_name = path + str(os.path.getsize(old_name) * 8)
    os.renames(old_name,new_name)