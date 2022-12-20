import json
import collections

def read_json(file_path, max_len_word=6, top_words=10): #читает файл и преобразовывает в словарь
    with open(file_path, encoding='utf-8') as news_file:
        news=json.load(news_file)
        description_words=[]
        for item in news['rss']['channel']['items']:
        #добавляем в список слова, которые длиннее 6 букв
            description=[word for word in item['description'].split(' ') if len(word)>max_len_word]
            description_words.extend(description)
            counter_words=collections.Counter(description_words)

        print(counter_words.most_common(top_words))
        # print(description_words)
            
        
        
        # print(news)

if __name__=='__main__':
    read_json('форматы данных/Files/newsafr.json')
