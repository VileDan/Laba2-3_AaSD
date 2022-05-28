import re
buffer_len = 1
work_buffer = ""
digit_flag = False
stop_flag = False
try:
    with open("text.txt", 'r+') as file:     # открываем файл
        print("\nРезультат работы программы\n")
        buffer = file.read(buffer_len)  # читаем символ
        if not buffer:  # если файл пустой
            print("\nФайл text.txt в директории проекта пустой.")
        while buffer:  # пока файл не пустой
            if not buffer:
                buffer = "."
                stop_flag = True
            if (buffer >= '0') and (buffer <= '9'):  # поиск числа
                work_buffer += buffer
                digit_flag = True
            if not re.findall(r'^[0-9]', buffer):
                if len(work_buffer) == 1:
                    digit_flag = False
                if digit_flag and not re.findall(r'[02468]{2,}|[13579]{2,}', work_buffer):  # обработка числа
                    print(work_buffer)
                    digit_flag = False
                    work_buffer = ''
                digit_flag = False
                work_buffer = ''
            if stop_flag:
                break
            buffer = file.read(buffer_len)  # читаем символ
            if not buffer:
                buffer = "."
                stop_flag = True
except FileNotFoundError:             # если файл пустой
    print("\nФайл text.txt в директории проекта не обнаружен.")
