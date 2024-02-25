# 1
'''
Записати у файл числа від 0 до 100
'''
with open("1.txt", 'w') as file:
    for i in range(0, 101):
        file.write(f"{i}\n")
# 2
'''
Прочитати текстовий файл назву якого має вказати користувач
'''
import os
while True:
    file_name = input("Enter file name, which you want open (for quit enter 'q'):")
    if file_name =='q':
        break
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            print(file.read())
    else:
        print("Incorrect file name!")

# 3
'''
Прочитати файл із зображення
Записати дані цього файлу під назвою 1.png
'''
with open('img.jpg', 'rb') as original_file, \
open('1.png', 'wb') as copied_file:
    copied_file.write(original_file.read())