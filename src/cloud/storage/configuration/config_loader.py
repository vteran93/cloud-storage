class ConfigLoader(object):

    __config = {
        'driver': '',
        'options': {
            'google':
                {'google_cloud_storage_key_path': ''},
            'amazon':
                {'amazon_cloud_storage_key_path': ''},
            'ftp': {
                'host': '',
                'port': '',
                'user': '',
                'password': '',
                'tls': False,
                },
            'ftp_tls': {
                'host': '',
                'port': '',
                'user': '',
                'password': '',
                'tls': True,
                },
            'sftp': {
                'host': '',
                'port': '',
                'user': '',
                'password': '',
                }
            'local':{
                'host': '',
                'port': ''
            }
        },
    }

    def get_config(self, driver):
        self.__config['driver'] = driver
        return self.__get_dict_config(self.__config['driver'])

    def __get_dict_config(self, driver):
        return self.__config['options'][driver]
