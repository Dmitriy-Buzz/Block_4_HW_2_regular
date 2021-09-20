import datetime
import json
import os

def decorator(old_func):

    log_dict = {}
    def new_func(*args, **kwargs):
        name_func = f'{old_func.__name__}'
        time = str(datetime.datetime.now())
        result = old_func(*args, **kwargs)
        log_dict = {'Time_func': time, 'Name_func': name_func, 'Arg_func': f"{args}, {kwargs}", 'Result': result}
        logs_f = input('Введите название файла для сохранения логов:')
        with open(f'{logs_f}{".json"}', 'a', encoding='utf-8') as f:
            json.dump(log_dict, f, ensure_ascii=False, indent=4)
        log = os.path.abspath(logs_f)
        print(f'Файлы расположены: {logs_f}{".json"}')
        return result
    return new_func