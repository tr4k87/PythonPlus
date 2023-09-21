from pathlib import Path
import os
def rename(endfile, extension, diap, koldigit, extend, path = '.'):
    count = 1 
    for file in os.listdir(path):
        if file.endswith(extension):
            Path(file).rename(f'{file[int(diap[0]):int(diap[1])]}{endfile}{"0"*int(koldigit)}{count}.{extend}')
            count += 1

if __name__ == '__main__':
    rename('sergey','txt', [3,6], 2, 'doc' )