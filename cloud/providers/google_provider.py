import os
from google.cloud import storage
from cloud.providers.base_provider import BaseProvider


class GoogleProvider(BaseProvider):

    __bucket = None
    __connection = None
    __blob_manager = None

    def __init__(self, *args, **kwargs):
        self.__connection = storage.Client.from_service_account_json(kwargs['google_cloud_storage_key_path'])

    def get_connection(self):
        return self.__connection

    def upload(self, butcket, filename, destination):
        self.__bucket = self.__connection.get_bucket(butcket)
        self.__blob_manager = self.__bucket.blob(destination)
        self.__blob_manager.upload_from_filename(filename)
        return self.__blob_manager.public_url

    def download(self, butcket, filename, destination):
        self.__bucket = self.__connection.get_bucket(butcket)
        self.__blob_manager = self.__bucket.blob(filename)
        self.__blob_manager.download_to_filename(destination)

    def exists(self, bucket, filename):
        self.__bucket = self.__connection.get_bucket(bucket)
        self.__blob_manager = self.__bucket.blob(filename)
        return self.__blob_manager.exists()

    def mkdir(self, bucket, path):
        path = self.__get_valid_path(path)
        self.__bucket = self.__connection.get_bucket(bucket)
        self.__blob_manager = self.__bucket.blob(path)
        self.__blob_manager.upload_from_string('')

    def pwd(self):
        if self.__bucket != None and self.__blob_manager != None:
            #import pdb; pdb.set_trace()
            return self.__blob_manager.path_helper(self.__bucket.path.__str__(), self.__blob_manager.name)
        return os.sep

    def cwd(self, bucket, destination):
        self.__bucket = self.__connection.get_bucket(bucket)
        self.__blob_manager = self.__bucket.blob(self.__get_valid_path(filename))

    def quit(self):
        del(self.__connection)
        del(self.__bucket)
        del(self.__blob_manager)

    def __get_valid_path(self, path):
        return path + os.sep if path[len(path)-1] != os.sep else path

if __name__ == "__main__":
    import os
    GOOGLE_JSON_KEY = os.getcwd() + os.sep + '../AKey.json'
    google_storage =  GoogleProvider()
    google_storage.upload('aBucket','captura.png','mi_captura.png')
    google_storage.download('aBucket', 'mi_captura.png', 'mi_captura_descargada.png')
    google_storage.mkdir('aBucket','mi_carpeta_creada')
    google_storage.mkdir('aBucket', 'carpeta2/')
    google_storage.pwd()

    print('existe %s' % google_storage.exists('aBucket', 'mi_carpeta_creada'))
    print('existe %s' % google_storage.exists('aBucket', 'mi_carpeta_creada/'))
    print('existe %s' % google_storage.exists('aBucket', 'mi_captura.png'))