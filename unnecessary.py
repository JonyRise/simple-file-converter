# Проєкт Конвертер файлів

# Користувач обирає файл який бажанє перекодувати (базовий файл)
# Користувач обирає файл у який необхідно перетворити
# Результат - файл обраного формату зі змістом базового файлу
from os import path

supported_formats = ['jpg', 'png', 'img', 'jpeg']
supported_format_str = ','.join(supported_formats)
    
def convert_file(file_name, new_format):
    with open(file_name, 'rb') as original_file,\
    open(f"{original_file.name.split('.')[0]}.{new_format}", 'wb') as formated_file:
        formated_file.write(original_file.read())
    print(f"File {original_file.name} successfully converted to {formated_file.name}")

while True:
    file_name = input("Enter file name which you want to convert (if you want quit enter 'q'): ")
    if file_name == 'q':
        break
    if not path.exists(file_name):
        print("File is not exists! Enter correct file name!")
        continue
    
    while True:
        format = input(f"Enter supported format({supported_format_str}) (if you want quit enter 'q'): ")
        if format == 'q':
            break
        if format in supported_formats:
            convert_file(file_name, format)
            break
        else:
            print(f"this format is not supported!Supported formats:{supported_format_str}")
