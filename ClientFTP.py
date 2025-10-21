from ftplib import FTP

import time
import threading

# Função responsavel por conectart ao Servidor(FTP) e listar diretorios.
def Connection(host, username, password):

   while True:

      try:

         ftp = FTP(host) # Conecatando no endereço do servidor
         ftp.login(user=username, passwd=password) # Autentição.

         print("=> Connectio sucessfully 200! \n")

         ftp.retrlines("LIST") # Liste os diretorios
#         root= "/"
#         print(f"[+] files {root}")
#         ftp.cwd(root)
         ftp.sendcmd("NOOP") # Pause o servidor

         time.sleep(300)

         ftp.quit() # Encerra a conexão com servidor

      except Exception as e:
         print(f"Error {e}")
         break

if __name__ == "__main__":
   host = "192.168.15.8"	# Endereço do servidor
   username = "squareroom_tech"		# Usuario do Servidor
   password = "ILoveYouFTP"	# Senha do Servidor

   # Thread para manter a conexão com o servidor.
   thread = threading.Thread(target=Connection, args=(host, username, password))
   thread.daemon = True
   thread.start()

   try:
      while True:
         time.sleep(1)
   except KeyboardInterrupt as e:
      print(f"Error {e}")

