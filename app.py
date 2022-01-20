####################################
#### FILE DECRYPTION (FOR TFS) #####
####################################
import os, time
from cryptography.fernet import Fernet

decrypt_key = '' # Put your decrypt key here

fernet = Fernet(decrypt_key)

time.sleep(1)
print(
"""
------
File Decryption
For TFS (Takeus File Sharing)
------
""")
time.sleep(1)

file_path = input('Path: ')
file_final = os.path.splitext(file_path)[0]

time.sleep(1)
print('\nplease wait')

# opening the encrypted file
with open('{}'.format(file_path), 'rb') as enc_file:
    encrypted = enc_file.read()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('{}'.format(file_final), 'wb') as dec_file:
    dec_file.write(decrypted)

## V1.0