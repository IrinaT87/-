import json

#чтение

with open ('форматы данных/Files/newsafr.json', encoding='utf-8') as f:
    json_data=json.load(f)
    news_list=json_data['rss']['channel']['items']
    for news in news_list:
        print(news['title'])
    print(f'Всего в файле {len(news_list)} новостей')

    print(type(news_list))
    print(type(json_data))

    #запись
    with open ('форматы данных/Files/newsafr2.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)