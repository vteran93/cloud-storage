import sys
from .providers.ftp_provider import FtpProvider
from .providers.sftp_provider import SFTPProvider
from .configuration.config_loader import ConfigLoader
from .providers.google_provider import GoogleProvider
from .providers.amazon_provider import AmazonProvider
from .exceptions.system_exceptions import UndefinedDriver, UnableToConnect, UnableToUploadFile, UnableToConnect


class FileSystem(object):

    __drivers = {
        'google': GoogleProvider,
        'amazon': AmazonProvider,
        'sftp': SFTPProvider,
        'ftp': FtpProvider,
        'ftp_tls': FtpProvider,
    }

    def __init__(self, driver, user_config={}):
        self.__set_connection(driver, user_config)

    def upload(self, bucket, filename, destination):
        try:
            return self.__connection.upload(bucket, filename, destination)

        except Exception as identifier:
            tb = sys.exc_info()[2]
            raise UnableToUploadFile('The requested file %s was unable to upload' %(filename)).with_traceback(tb)

    def download(self, butcket, filename, destination):
        try:
            self.__connection.download(butcket, filename, destination)
        except Exception as identifier:
            tb = sys.exc_info()[2]
            raise UnableToUploadFile('The requested file %s was unable to download' %(filename)).with_traceback(tb)

    def exists(self, bucket, path=''):
        try:
            return self.__connection.exists(bucket, path)
        except Exception as identifier:
            tb = sys.exc_info()[2]
            raise UnableToConnect('I have a problem to check if %s exists' %(path)).with_traceback(tb)

    def mkdir(self, bucket, filename):
        try:
            return self.__connection.exists(bucket, filename)
        except Exception as identifier:
            tb = sys.exc_info()[2]
            raise UnableToConnect('I have a problem to create %s ' %(filename)).with_traceback(tb)

    def pwd(self):
        return self.__connection.pwd()

    def cwd(self, bucket, destination):
        return self.__connection(bucket, destination)

    def quit(self):
        return self.__connection.quit()

    def __set_connection(self, driver, user_config):
        try:
            self.__connection = self.__get_connection(driver, user_config)
        except Exception as identifier:
            tb = sys.exc_info()[2]
            raise UnableToConnect('The driver '+driver+' was unable to connect with error '+ identifier.__str__()).with_traceback(tb)

    def __get_connection(self, driver, user_config):
        driver_provider = self.__get_provider(driver)
        configuration_for_class = self.__get_config(driver, user_config)

        return self.__start_connection(driver_provider, configuration_for_class)

    def __start_connection(self, driver_provider, configuration_params):
        return driver_provider(**configuration_params)

    def __get_provider(self, driver):
        if driver in self.__drivers.keys():
            return self.__drivers.get(driver)

        raise UndefinedDriver('Unable to find specified driver', driver)

    def __get_config(self, driver, user_config):
        config = ConfigLoader()
        base_config = config.get_config(driver)
        base_config.update(user_config)

        return base_config

if __name__ == "__main__":
    connection_params = {
        'host': '192.168.10.10',
        'port': 21,
        'user': 'vsftp',
        'password': 'secret',
        'tls': True,
    }
    instanceF = FileSystem('ftp', connection_params)
