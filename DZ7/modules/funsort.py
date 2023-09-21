import os
from pathlib import Path
import shutil




def fun_sort():
    os.chdir('my_folder')
    if not os.path.exists('doc'):
        os.mkdir('doc')
    for file in os.listdir('.'):
        if file.endswith(('txt', 'doc', 'xls')):
            shutil.copy(file, 'doc')
            # old_file = Path(file)
            # new_file = old_file.replace(Path.cwd() / 'doc' / old_file)