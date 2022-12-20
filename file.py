# f=open('text.txt', 'r')
# # res=f.read()  #считываем полностью
# # res=f.readline() #считываем по одной строке
# # res1=f.readline()
# print(res)
# print(res1)
# f.close()
with open ('text.txt') as f: #контекстный менеджер
    res=f.readlines() #считывает как список строк с разделителями
    print(res) #обращение по индексу

# with open ('text.txt') as f: #выводим по одной строке в цикле
#     for line in f:
#         print(line)

# with open ('text2.txt', 'a') as file:
#     # file.write('\nHello World!') #запись по одной строке
#     file.writelines(['line1\n', 'line2\n', 'line3\n']) #запись нескольких строк, передаем список
# with open ('text3.txt', 'x') as file:
#     file.write('test')

#Загружаем картинку из интернета
# 
with open('text3.txt', 'w', encoding='utf-8') as file:
    file.write('Привет!')

