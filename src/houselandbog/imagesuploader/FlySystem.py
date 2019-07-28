from Providers.FtpProvider import FtpProvider

class FlySystem(object):
    def __init__(self, *args):
        super(FlySystem, self).__init__(*args)

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
        passs

    def __configure(self, driver):
        drivers = {
            'google':''
            'ftp': FtpProvider
            'ftp_tls': ''
            'sftp':''
            }
        return drivers.get(driver, )