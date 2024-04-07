import os
import pyaes

## abrir arquivo encripitado

file_name = 'text.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descripitografia

key = b"testransomware"
aes = pyaes.AESModeOfOperationCTR(key)
decypt_data = aes.decrypt(file_data)

## remover o arquivo cripitografado

os.remove(file_name)

## criar arquivo descripitografado
new_file = 'text.txt'
new_file = open(f'{new_file}', "wb")
new_file.write(decypt_data)
new_file.close()