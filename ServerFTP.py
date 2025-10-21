from pyftpdlib.authorizers import DummyAuthorizer # gerenciar usuario e suas permições.
from pyftpdlib.servers import FTPServer # Abrir um servidor.
from pyftpdlib.handlers import FTPHandler # Controle de cada conexão.

# Configurando usuario, senha, diretorio e acesso.
authorizer = DummyAuthorizer
authorizer.add_user("squareroom_tech", "ILoveYouFTP", "..//server", perm="elradfmw")

# Configurando o controlador de conexões, lidar com cada conexão.
handler = FTPHandler

# Endeço do servidor.
address = ("192.168.15.8", 2121)

# vinculando o endereco e o controlador.
server = (address, handler)
server.serve_forever() # Servidor rodando!

# dependecies.
# pip install pyftpdlib --upgrade
