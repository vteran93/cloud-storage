import inspect

class UrlMaker(object):
    host = None
    port = None
    user = None
    protocol = None
    password = None

    def __init__(self, protocol, host, user, password, port):
        self.protocol = protocol
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def get_url(self, bucket, destination):
        complete_destination_path = "%s/%s" % (bucket, destination)
        return "%s://%s%s:%s/%s" % (self.protocol, self.__get_authority(),
                                  self.__get_host(), self.port, complete_destination_path)

    def __get_authority(self):

        if(self.user is not None and self.password is not None):
            return "%s:%s" % (self.user, self.password)
        elif(self.user is not None):
            return "%s" % (self.user)
        else:
            return ""

    def __get_host(self):
        if self.user is not None:
            return '@%s' % (self.host)

        return '%s' % (self.host)
