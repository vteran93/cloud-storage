
from providers.FtpProvider import FtpProvider
from providers.SFTPProvider import SFTPProvider
from configuration.ConfigLoader import ConfigLoader
from providers.GoogleProvider import GoogleProvider
from providers.AmazonProvider import AmazonProvider
from Exceptions.SystemExceptions import UndefinedDriver, UnableToConnect


class FileSystem(object):

    __drivers = {
        'google': GoogleProvider,
        'amazon': AmazonProvider,
        'sftp': SFTPProvider,
        'ftp': FtpProvider,
        'ftp_tls': FtpProvider,
    }

    __connection = None

    def __init__(self, driver, user_config={}):
        self.__set_connection(driver, user_config)

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

    def __set_connection(self, driver, user_config):
        try:
            self.__connection = self.__get_connection(driver, user_config)
        except Exception as identifier:
            raise UnableToConnect('The driver was unable to connect with error', [driver, identifier])

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
        #import pdb; pdb.set_trace()
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
