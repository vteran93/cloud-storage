import os
import pysftp
from .base_provider import BaseProvider
from .url_maker import UrlMaker

class SFTPProvider(BaseProvider):

    __protocol= 'sftp'

    def __init__(self, host, port, user, password=None):
        self.__connection = pysftp.Connection(host, username=user, password=password)
        self.__url_maker = UrlMaker(self.__protocol, host, user, password, port)

    def upload(self, butcket, file_name, destination_folder=''):
        real_file_name = self.__get_real_file_name(file_name)
        self.__connection.put(file_name, "%s%s%s%s" %(butcket, os.sep, destination_folder, real_file_name))
        
        return self.__url_maker.get_url(butcket, destination_folder)

    def download(self, butcket, filename, destination=''):
        remote_path = "%s%s%s" % (butcket, os.sep, filename)
        
        return self.__connection.get(remote_path, destination)

    def exists(self, bucket, filename):
        return self.__connection.exists('%s%s%s' % (bucket, os.sep, filename))
    
    def mkdir(self, bucket, path):
        if(not self.exists(bucket, path)):
            return self.__connection.mkdir("%s%s" % (bucket, path))
        else:
            raise IOError('Directory %s already exists on %s' %(path, bucket))
    
    def pwd(self):
        return self.__connection.pwd()

    def cwd(self, bucket, destination):
        return self.__connection.cd(bucket + os.sep + destination)

    def quit(self):
        return self.__connection.close()

    def __get_url(self, bucket, destination):
        return self.__url_maker.get_url(bucket, destination)

    def __get_real_file_name(self, file_name):
        return file_name.split(os.sep).pop()

if __name__ == "__main__":
    sftp = SFTPProvider("192.168.10.10", '22', 'vagrant')
    sftp.upload('test', 'captura.png',)
    sftp.download('test', 'captura.png')
    print( 'mi alma ' + sftp.exists('test', 'mi alma.png').__str__())
    print( 'captura ' + sftp.exists('test', 'captura.png').__str__())
    print( 'captura ' + sftp.exists('test', 'captura/').__str__())
    print( 'directorio ' + sftp.exists('test', 'directorio/').__str__())
    try:
        print( 'directorio ' + sftp.mkdir('test', 'midirectorio').__str__())
        print( 'directorio ' + sftp.exists('test', 'midirectorio').__str__())
    except Exception as identifier:
        print('el directorio ya existe todo ok')