from configparser import ConfigParser
from providers.FtpProvider import FtpProvider
from providers.SFTPProvider import SFTPProvider
from providers.GoogleProvider import GoogleProvider
from providers.AmazonProvider import AmazonProvider
from Exceptions.SystemExceptions import UndefinedDriver


class FileSystem(object):

    __drivers = {
        'google': 'GoogleProvider',
        'amazon': 'AmazonProvider',
        'sftp': 'SFTPProvider',
        'ftp': 'FtpProvider',
        'ftp_tls': 'FtpProvider',
    }

    __connection = None

    def __init__(self, driver, *args, **kwargs):
        self.__base_config = self.__get_config()
        import pdb; pdb.set_trace()

        self.__connection = self.__get_connection('driver')()

    def upload(self,):
        pass
    
    def download(self, ):
        pass

    def exists(self, ):
        pass
    
    def mkdir(self):
        pass
    
    def pwd(self):
        pass
    
    def quit(self):
        pass

    def __get_connection(self, driver):
        driverProvider = self.__drivers.get(driver, self.__exception(driver))


    def __exception(self, driver):
        raise UndefinedDriver('Unable to find specified driver', driver)
    
    def __get_config(self):
        config = ConfigParser()
        config.read('config/configuration.ini')
        return config

if __name__ == "__main__":
    instanceF = FileSystem('google')
