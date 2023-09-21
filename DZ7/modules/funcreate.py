import random as rnd
from pathlib import Path


def fun_create(extension, min_len = 6, max_len = 30, max_size = 4096, gen = 42):
    for _ in range(int(gen)):
        count = 0
        res = ''
        for _ in range(rnd.randint(min_len, max_len)):
            a = chr(rnd.randint(97, 122))
            res += a
        name = res + '.' + extension
        f = open(name, 'a', encoding='utf-8')
        f.close()
        old_file = Path(name)
        new_file = old_file.replace(Path.cwd() / 'my_folder' / old_file)
        count += 1

def create_file(extension):
    for key in extension:
        fun_create(extension=extension[key] , gen = key )


if __name__ =='__main__':
    fun_create('txt')