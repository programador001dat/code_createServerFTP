from ftplib import FTP

import os

# Informações do Servidor FTP.
FTP_HOST = "192.168.15.8"
FTP_PORT = 2121
FTP_USER = "squareroom_tech"
FTP_PASSWD = "ILoveYouFTP"


# Caminho do seu arquivo a ser enviado.
file_local = "./sendFile.txt"
file_remote = "sendFile2.txt"

# Verifica se o arquivo local existe.
if not os.path.exists(file_local):
   print(f"Error file not exist in directory {file_local}")

else:

   try:

      # Conectando ao servidor.
      ftp = FTP()
      ftp.connect(FTP_HOST, FTP_PORT)
      ftp.login(FTP_USER, FTP_PASSWD)

      # Lista os arquivos no servidor FTP.
      with open(file_local, "rb")as f:
         ftp.storbinary(f"STOR {file_remote}", f)

      print("Upload sucess 200!")

      ftp.quit()

   except Exception as e:
      print(f"Error {e}")
