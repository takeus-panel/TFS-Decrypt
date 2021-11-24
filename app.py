###########################################
#### APP FOR DECRYPTION (FILE MANAGER) ####
###########################################
import os, time
from cryptography.fernet import Fernet

decrypt_key = '6jd6N2h0UAEboT6MSlWIfgMoYlg4CL94_ReA6PCLMWA='
fernet = Fernet(decrypt_key)

time.sleep(1)
print(
"""
------
App for file decryption (file manager)
Takeus 2021
------
""")

file_path = input('File: ')

# opening the encrypted file
with open('{}'.format(file_path), 'rb') as enc_file:
    encrypted = enc_file.read()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('{}'.format(file_path), 'wb') as dec_file:
    dec_file.write(decrypted)

