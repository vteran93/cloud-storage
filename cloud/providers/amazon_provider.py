
from cloud.providers.base_provider import BaseProvider


class AmazonProvider(BaseProvider):
    def __init__(self, *args):
        super(AmazonProvider, self).__init__(*args)
