# Проєкт Конвертер файлів

# Користувач обирає файл який бажанє перекодувати (базовий файл)
# Користувач обирає файл у який необхідно перетворити
# Результат - файл обраного формату зі змістом базового файлу
from os import path

supported_formats = ['jpg', 'png', 'img', 'jpeg']
while True:
    file_name = input("Enter file name which you want to convert (if you want quit enter 'q'): ")
    if file_name == 'q':
        break
    if path.exists(file_name):
        supported_format_str = ','.join(supported_formats)
        while True:
            format = input(f"Enter supported format({supported_format_str}) (if you want quit enter 'q'): ")
            if format == 'q':
                break
            if format in supported_formats:
                with open(file_name, 'rb') as original_file,\
                open(f"{original_file.name.split('.')[0]}.{format}", 'wb') as formated_file:
                    formated_file.write(original_file.read())
                print(f"File {original_file.name} successfully converted to {formated_file.name}")
                break
            else:
                print(f"this format is not supported!Supported formats:{supported_format_str}")
    else:
        print("File is not exists! Enter correct file name!")

