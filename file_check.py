import sys
import os.path
import hashlib


def get_hash_sum(file_path, algorithm):
    with open(file_path, 'rb') as f:
        d = f.read()
    hash_sum = ''
    if algorithm == 'md5':
        hash_sum = hashlib.md5(d).hexdigest()
    elif algorithm == 'sha1':
        hash_sum = hashlib.sha1(d).hexdigest()
    elif algorithm == 'sha256':
        hash_sum = hashlib.sha256(d).hexdigest()
    return hash_sum


def check_file(*args):
    args = args[0]
    if len(args) != 3:
        print('Неверная запись.')
    else:
        file_path = sys.argv[2] + '\\' + args[0]
        if not os.path.exists(file_path):
            print(args[0] + ' NOT FOUND')
        else:
            algorithm = args[1]
            if algorithm != 'md5' and algorithm != 'sha1' and algorithm != 'sha256':
                print(args[0] + ' Неверная хэш функция.')
            else:
                need_hash_sum = args[2].replace('\n', '')
                return_hash_sum = get_hash_sum(file_path, algorithm)
                if need_hash_sum != return_hash_sum:
                    print(args[0] + ' FAIL')
                else:
                    print(args[0] + ' OK')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Неверное число параметров.')
    else:
        if not os.path.exists(sys.argv[1]):
            print('Указанного файла не существует.')
        else:
            if not os.path.exists(sys.argv[1]):
                print('Указанной директории не существует.')
            else:
                with open(sys.argv[1], 'r', encoding='utf-8') as file:
                    data = file.readlines()
                for line in data:
                    if line != '\n':
                        check_file(line.split(' '))
