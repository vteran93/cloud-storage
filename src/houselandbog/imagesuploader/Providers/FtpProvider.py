from BaseProvider import BaseProvider
from ftplib import FTP
from ftplib import FTP_TLS
import os

class FtpProvider(BaseProvider):

    def __init__(self, host, port, user, password, tls=False):
        self.ftp_conn = self.__connect(host, port, user, password, tls=False)

    def upload(self, butcket, filename):
        return self.ftp_conn.storbinary('STOR %s%s%s'% (butcket, os.sep, filename), open(filename, 'rb'))

    def download(self, butcket, filename, destination):
        handle = open(destination + os.sep + filename, 'wb')
        return self.ftp_conn.retrbinary('RETR %s%s%s' % (butcket, os.sep, filename), handle.write)

    def exists(self, bucket, filename):
        return self.__exists_folder(bucket, filename) or self.__exists_file(bucket, filename)

    def mkdir(self, bucket, path):
        if(not self.exists(bucket, path)):
            return self.ftp_conn.mkd('%s%s%s' % (bucket, os.sep, path))
        else:
            raise Exception('Directory %s already exists on %s' %(path, bucket))

    def pwd(self):
        return self.ftp_conn.pwd()

    def quit(self):
        return self.ftp_conn.quit()

    def __connect(self, host, port, user, password, tls=False):
        if(tls):
            return self.__connectTls(host, user, password)
        else:
            return self.__connectFtp(host, port, user, password)

    def __connectTls(self, host, user, password):
        ftp_tls = FTP_TLS(host, user, password)
        #ftp_tls.sendcmd('USER %s' % user)
        #ftp_tls.sendcmd('PASS %s' % password)
        
        return ftp_tls

    def __connectFtp(self, host, port, user, password):
        ftp = FTP(host=host, user=user, passwd=password)

        return ftp
    
    def __exists_folder(self, bucket, filename):
        try:
            self.ftp_conn.cwd(bucket + os.sep + filename)
            self.ftp_conn.cwd('/')

            return True
        except Exception as identifier:
            return False
    
    def __exists_file(self, bucket, filename):
        try:
            return self.ftp_conn.size(bucket + os.sep + filename) > 0
        except Exception as identifier:
            return False

if __name__ == "__main__":

    ftp = FtpProvider('192.168.10.10', 22, 'vsftp', 'secret', True)
    ftp.upload('test', 'captura.png')
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
