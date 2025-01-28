import os
import pyaes

# Abre o arquivo criptografado (teste.txtcriptografado) em modo de leitura binária (rb) e lê todo o seu conteúdo.

file_name = 'teste.txtcriptografado'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Define a chave de descriptografia (testeransonwares) e cria uma instância do AES no modo CTR (Counter) usando a biblioteca pyaes.

key = b'testeransonwares'
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografa os dados do arquivo usando a chave de descriptografia.

decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado (teste.txtcriptografado) do sistema.

os.remove(file_name)

# Criar um novo arquivo descriptografado(teste.txt) em modo de escrita binaria(wb) e grava os dados descriptografados nele.
new_file = 'teste.txt'
new_file = open(new_file, 'wb')
new_file.write(decrypt_data)
new_file.close()
