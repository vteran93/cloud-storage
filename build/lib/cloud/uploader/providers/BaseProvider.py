from abc import abstractmethod
from abc import ABC as AbstractClass


class BaseProvider(AbstractClass):

    __connection = None

    def __init__(self, host, port, user, password):
        raise NotImplementedError()

    @abstractmethod
    def upload(self, butcket, filename, destination):
        raise NotImplementedError()

    @abstractmethod
    def download(self, butcket, filename, destination):
        raise NotImplementedError()
    
    @abstractmethod
    def exists(self, bucket, filename):
        raise NotImplementedError()
    
    @abstractmethod
    def mkdir(self, bucket, path):
        raise NotImplementedError()

    @abstractmethod
    def pwd(self):
        raise NotImplementedError()

    @abstractmethod
    def quit(self):
        raise NotImplementedError()