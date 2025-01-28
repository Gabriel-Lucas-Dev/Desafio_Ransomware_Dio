# Desafio_Ransomware_Dio

Este repositório contém dois scripts Python para criptografar e descriptografar arquivos usando a biblioteca `pyaes`.

## Requisitos

- Python 3.x
- Biblioteca `pyaes`

## Instalação
 Instale o Python:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```
## Crie um ambiente Virtual
 - Obs: execute os seguintes comandos no diretorio que estão os arquivos Decrypter, Encrypter e teste.txt
  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
```
## Instale a Biblioteca `pyaes`
  ```bash
  pip install pyaes
  ```
## Criptografar um arquivo
```bash
python encrypter.py
```
## Descriptografar o arquivo
```bash
python decrypter.py
```
## Detalhamento dos Scripts
encrypter.py:

  - Este script criptografa um arquivo chamado `teste.txt` usando a biblioteca `pyaes`.

decrypter.py:

  - Este script descriptografa o arquivo criptografado `teste.txtcriptografado` usando a mesma chave de criptografia.
