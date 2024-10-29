from stellar_sdk import Keypair
import requests

# Gerando um par de chaves (privada e pública)
pair = Keypair.random()

# Exibindo a chave secreta e pública
print(f"Secret: {pair.secret}")
print(f"Public Key: {pair.public_key}")

# Enviando a chave pública para o Friendbot (Testnet) para criar a conta
public_key = pair.public_key
response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")

# Verificando se a conta foi criada com sucesso
if response.status_code == 200:
    print("SUCCESS! You have a new account :)")
    print(response.json())  # Exibindo detalhes da transação
else:
    print("Error! Could not create account.")
