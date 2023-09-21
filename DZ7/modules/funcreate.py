import random as rnd

def fun_create(extension, min_len = 6, max_len = 30, max_size = 4096, gen = 42):
    for _ in range(gen):
        count = 0
        res = ''
        for _ in range(rnd.randint(min_len, max_len)):
            a = chr(rnd.randint(97, 122))
            res += a
        open(f'{res}.{extension}', 'a', encoding='utf-8')
        count += 1




if __name__ =='__main__':
    fun_create('txt')