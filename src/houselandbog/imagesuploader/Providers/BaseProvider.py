from abc import ABC as AbstractClass
from abc import abstractmethod


class BaseProvider(AbstractClass):
    def __init__(self, host, port, user, password, tls=False):
        pass

    @abstractmethod
    def upload(self, butcket, filename):
        pass

    @abstractmethod
    def download(self, butcket, filename, destination):
        pass
    
    @abstractmethod
    def exists(self, bucket, filename):
        pass
    
    @abstractmethod
    def mkdir(self, bucket, path):
        pass

    @abstractmethod
    def pwd(self):
        pass

    @abstractmethod
    def quit(self):
        pass