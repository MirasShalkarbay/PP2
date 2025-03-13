#1
import os

path = r'D:\prog\lab'

for root, dirs, files in os.walk(path):
    print(root)
    print(dirs)
    print(files)

#2
import os

path_dir = input()

if os.path.exists(path_dir):
    print('exist')

    if os.access(path_dir, os.R_OK):
        print('readbale')
    else:
        print('not readbale')

    if os.access(path_dir, os.W_OK):
        print('writable')
    else:
        print('not writable')

    if os.access(path_dir, os.X_OK):
        print('executable')
    else:
        print('not executable')
else:
    print('not exist')

#3
import os

path_dir = input()

if os.path.exists(path_dir):
    print('Exists')

    filename = os.path.basename()
    dirname = os.path.dirname()

    print(f"Name of file is: {filename}")
    print(f"Path is: {dirname}")
else:
    print('Not exist')

#4
import os

with open('c.txt', 'r' ,encoding = 'UTF-8') as f:
    line_count = len(f.readlines())
    print(line_count)


#5
import os

myList = [i for i in range(5)]

with open('c.txt', 'wt', encoding = 'UTF-8') as fl:
    for i in myList:
        fl.write(str(i) + '\n')

#6 Ex
import os

folder_path = r'D:\prog\lab\lab6\alphabet'

for i in range(26):
    b = chr(65 + i)
    
    file_name = b + '.txt'
    full_path = os.path.join(folder_path, file_name)


    with open(full_path, 'w') as files:
        files.write(f'The file name is {file_name}')

#7 Ex

import shutil

shutil.copy('c.txt', 'cc.txt')

#8 Ex
import os

path_dir = input()

if os.path.exists(path_dir):
    if os.path.isfile(path_dir):
        print('File exists')

        if os.access(path_dir, os.R_OK):
            print('Readable')
        else:
            print('not readable')

        if os.access(path_dir, os.W_OK):
            print('Writable')
        else:
            print('Not Writable')
    
        os.remove(path_dir)
        print('The file has been deleted')
    else:
        print('File does not exists')
else:
    print('Path does not exists')