import os
from ftplib import FTP
from ftplib import FTP_TLS
from .base_provider import BaseProvider
from .url_maker import UrlMaker

class FtpProvider(BaseProvider):

    __protocol = 'ftp'
    __host = ''
    __port = ''

    def __init__(self, host, port, user, password, tls=False):
        self.__host = host
        self.__port = port
        self.__connection = self.__connect(host, port, user, password, tls)
        self.__url_maker = UrlMaker(self.__protocol, host, user, password, port)

    def upload(self, butcket, filename, destination):
        self.__connection.storbinary('STOR %s%s%s'% (butcket, os.sep, destination), open(filename, 'rb'))

        return self.__get_url(butcket, destination)

    def download(self, butcket, filename, destination):
        handle = open(destination + os.sep + filename, 'wb')
        
        return self.__connection.retrbinary('RETR %s%s%s' % (butcket, os.sep, filename), handle.write)

    def exists(self, bucket, filename):
        return self.__exists_folder(bucket, filename) or self.__exists_file(bucket, filename)

    def mkdir(self, bucket, path):
        if(not self.exists(bucket, path)):
            return self.__connection.mkd('%s%s%s' % (bucket, os.sep, path))
        else:
            raise IOError('Directory %s already exists on %s' %(path, bucket))

    def pwd(self):
        return self.__connection.pwd()

    def cwd(self, bucket, destination):
        self.__connection.cwd(bucket + os.sep + destination)

    def quit(self):
        return self.__connection.quit()

    def __connect(self, host, port, user, password, tls=False):
        if(tls):
            return self.__connectTls(host, user, password)
        else:
            return self.__connectFtp(host, port, user, password)

    def __connectTls(self, host, user, password):
        ftp_tls = FTP_TLS(host)
        ftp_tls.login(user, password)

        ftp_tls.prot_p()

        return ftp_tls

    def __connectFtp(self, host, port, user, password):
        ftp = FTP(host=host, user=user, passwd=password)

        return ftp

    def __exists_folder(self, bucket, filename):
        try:
            self.__connection.cwd(bucket + os.sep + filename)
            self.__connection.cwd('/')

            return True
        except Exception as identifier:
            return False

    def __exists_file(self, bucket, filename):
        try:
            return self.__connection.size(bucket + os.sep + filename) > 0
        except Exception as identifier:
            return False

    def __get_url(self, bucket, destination):
        return self.__url_maker.get_url(bucket, destination)

if __name__ == "__main__":

    ftp = FtpProvider('192.168.10.10', 21, 'vsftp', 'secret', True)
    ftp.upload('test', 'captura.png', 'uploaded_captura.png')
    ftp.download('test', 'captura.png', '/home/victor/')
    print( 'mi alma ' + ftp.exists('test', 'mi alma.png').__str__())
    print( 'captura ' + ftp.exists('test', 'captura.png').__str__())
    print( 'captura ' + ftp.exists('test', 'captura/').__str__())
    print( 'directorio ' + ftp.exists('test', 'directorio/').__str__())
    try:
        print( 'directorio ' + ftp.mkdir('test', 'midirectorio').__str__())
        print( 'directorio ' + ftp.exists('test', 'midirectorio').__str__())
    except Exception as identifier:
        print('el directorio ya existe todo ok')
