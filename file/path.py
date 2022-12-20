import os #библиотека, которая позволяет работать с путями 
file_name='log.txt'
file_log_dir='logs'
root_path=os.getcwd()
full_path=os.path.join(root_path, file_log_dir, file_name)
print(full_path)
print()

with open(full_path, 'a') as file:
    file.write('\nHello, world!' ) #запись в файл с указанием переменной, в которой записан путь, вместо полного пути 