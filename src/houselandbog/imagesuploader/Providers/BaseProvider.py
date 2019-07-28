from abc import ABCMeta
from abc import abstractmethod


class BaseProvider(ABCMeta):
    def __init__(self, *args):
        super(BaseProvider, self).__init__(*args))

    @abstractmethod
    def upload(self, parameter_list):
        pass

    @abstractmethod
    def download(self, parameter_list):
        pass
    
    @abstractmethod
    def exists(self, parameter_list):
        pass
    
    @abstractmethod
    def mkdir(self, parameter_list):
        pass

    @abstractmethod
    def pwd(self, parameter_list):
        pass

    @abstractmethod
    def quit(self, parameter_list):
        pass