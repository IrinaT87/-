import requests

# token="y0_AgAAAAAc0-O4AADLWwAAAADXN203nF4gJAWIRauwDpKQ-Drek3Q6FhM"
from settings import token

class Yandex:
    
    host='https://cloud-api.yandex.net'

    
    def __init__(self, token):
        self.token=token

    def get_headers(self):
        return {'Content_Type':'application/json', 'Authorization':f'OAuth {self.token}'}

    def get_files_list(self):
        uri='/v1/disk/resources/files'
        url=self.host+uri
        headers=self.get_headers()
        params={'limit':1}
        response=requests.get(url, headers=headers, params=params)
        print(response.json())
        print(response.status_code)
        

    def create_folder(self):
        uri='/v1/disk/resources/'
        url=self.host+uri
        params={'path':'/test_folder'}
        response=requests.put(url, headers=self.get_headers(),params=params)
        print(response.json())
        print(response.status_code)

    def get_upload_link(self,disk_file_name):
        uri='/v1/disk/resources/upload'
        url=self.host+uri
        params={'path':f'/{disk_file_name}'}
        response=requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']
        # print(response.json())
        # print(response.status_code)
        # print(response.json()['href'])


    def upload_from_pc(self, local_file_name, disk_file_name):
        upload_link=self.get_upload_link(disk_file_name)
        response=requests.put(upload_link,headers=self.get_headers(), data=open(local_file_name, 'rb'))
        print(response.status_code)
        if response.status_code== 201:
            print('Загрузка прошла успешно')


ya=Yandex(token)
# ya.get_files_list()
# ya.create_folder()
# ya.get_upload_link('file3.json')
ya.upload_from_pc('test.json','file3.json')