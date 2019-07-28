"""
Esta clase debe decidir el driver con el cual se va a conectar
y retornar la instancia correspondiente
"""
class ConnectionProvider(object):
    def __init__(self, *args):
        super(ConnectionProvider, self).__init__(*args))
    
