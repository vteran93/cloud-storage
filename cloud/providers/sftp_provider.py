import os
import pysftp
from cloud.providers.base_provider import BaseProvider
from cloud.providers.url_maker import UrlMaker

class SFTPProvider(BaseProvider):

    def __init__(self, host, port, user, password=None):
        #super(SFTPProvider, self).__init__(*args))
        self.__connection = pysftp.Connection(host, username=user, password=password)
        self.__url_maker = UrlMaker(self.__protocol, host, user, password, port)

    def upload(self, butcket, filename, destination=''):
        return self.__connection.put(filename, "%s%s%s%s" %(butcket, os.sep, destination,filename))

    def download(self, butcket, filename, destination=''):
        return self.__connection.get("%s%s%s%s" %(butcket, os.sep, filename, destination), destination)

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