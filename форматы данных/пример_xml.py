import xml.etree.ElementTree as ET

parser=ET.XMLParser(encoding='utf-8')
tree=ET.parse('форматы данных/Files/newsafr.xml', parser)
root=tree.getroot()
# print(root)
# print(root.tag)
# print(root.text)
# print(root.attrib)

#чтение новостей, вывод title
# news_list=root.findall('channel/item')
# # for news in news_list:
#     # print(news) #вывод адресов ячеек памяти item
#     title=news.find('title')
#     # print(title) #вывод адресов ячеек памяти title
#     print(title.text) #добавляем свойство text для вывода текста
# print(f'Всего в файле {len(news_list)} новостей')

#если не нужны все новости, а только title или любой другой раздел
# titles_list=root.findall('channel/item/title')
# for title in titles_list:
#     print(title.text)
# print(f'Всего в файле {len(titles_list)} новостей')

# tree.write('форматы данных/Files/newsafr2.xml') #запись 

#Если нужен title и description, и мы знаем что они есть

# titles_list=root.findall('channel/item/title')
# descr_list=root.findall('channel/item/description')

# for title, descr in zip(titles_list, descr_list):
#     print(title.text, descr.text)

#если не знаем есть ли title, description. вариант с проверкой
news_list=root.findall('channel/item')
if news_list!=None:
    for news in news_list:
        title=news.find('title')
        descr=news.find('description')
        if title!=None and descr!=None:
            print(title.text, descr.text)

   
