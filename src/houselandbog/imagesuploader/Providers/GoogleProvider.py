
from BaseProvider import BaseProvider


class GoogleProvider(BaseProvider):
    """
    def __init__(self, *args):
        super(GoogleProvider, self).__init__(*args))
    """

    def __init__(self, host, port, user, password):
        raise NotImplementedError()

    def upload(self, butcket, filename, destination):
        raise NotImplementedError()

    def download(self, butcket, filename, destination):
        raise NotImplementedError()
    
    def exists(self, bucket, filename):
        raise NotImplementedError()
    
    def mkdir(self, bucket, path):
        raise NotImplementedError()

    def pwd(self):
        raise NotImplementedError()

    def quit(self):
        raise NotImplementedError()
