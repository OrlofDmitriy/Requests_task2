import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

        replace = True
        res = requests.get(f'{url}/upload?path={file_path}&overwrite={replace}', headers=headers).json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
                print('Готово!')
            except KeyError:
                print(res)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r"\Users\Orlof\Pictures\639.jpg"
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
