import csv

# with open ('форматы данных/Files/newsafr.csv', encoding='utf-8') as f:
#     reader=csv.reader(f)
# for row in reader:
    #     # print(row)

    #вывод заголовков новостей без названия колонки  (title)
# import csv

# with open ('форматы данных/Files/newsafr.csv', encoding='utf-8') as f:
#     reader=csv.reader(f)
#     count=-1
#     for row in reader:
#         count+=1
#         if count==0:
#             continue
        
#         print(row[-1])
# print(f'Всего в файле {count} новостей')

#1 способ - вывод всего файла целиком, вывод 1х трех элементов
# with open ('форматы данных/Files/newsafr.csv', encoding='utf-8') as f:
#     reader=csv.reader(f)
#     new_list=list(reader)  #получаем список со вложеными списками
#     print(new_list[:3])

    #2 способ - вывод всего файла целиком, заголовок убирааем в отдельную переменную header 
    # для дальнейшего использования
# with open ('форматы данных/Files/newsafr.csv', encoding='utf-8') as f:

#     reader=csv.reader(f)
#     news_list=list(reader)  #получаем список со вложеными списками
#     header=news_list.pop(0)  #забираем 0-й элемент из списка и помещаем его в переменную
#     for news in news_list:
#         print(news[-1])
#     print(f'Всего в файле {len(news_list)} новостей')
#     print(header)

#3 способ - вывод всего файла целиком, но в виде словаря, где ключ-название колонки, 
# значение-содержание колонки
# with open ('форматы данных/Files/newsafr.csv', encoding='utf-8') as f:
#     reader=csv.DictReader(f)
#     count=0
#     for row in reader:
#         count+=1
#         print(row)
#     print(type(row))
# print(f'Всего в файле {count} новостей')

#запись в файл. сначала считали файл
with open ('форматы данных/Files/newsafr.csv', encoding='utf-8') as f:

    reader=csv.reader(f)
    news_list=list(reader)  #получаем список со вложеными списками
    header=news_list.pop(0)

# with open ('форматы данных/Files/newsafr2.csv', 'w', encoding='utf-8') as f: #запись построчно
#     writer=csv.writer(f)
#     writer.writerow(header)
#     for row in news_list:
#         writer.writerow(row)

with open ('форматы данных/Files/newsafr3.csv', 'w', encoding='utf-8') as f: #запись всего файла
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(news_list)

#параметры форматирования
writer=csv.writer(f, delimiter=';') #задаем разделитель
writer=csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL) #ставит кавычки только там, 
#где они нужны, те если есть знак препинания, а не разделитель
writer=csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL) #закавычивает все
writer=csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\') #запрет кавычек,
# вместо кавычек-два обратных слэша

csv.register_dialect('commas_no_quote',delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
csv.register_dialect('semicolon_quoteall',delimiter=';', quoting=csv.QUOTE_ALL, escapechar='\\')

