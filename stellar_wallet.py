from stellar_sdk import Keypair
import requests

# Generate a keypair (private and public keys)
keypair = Keypair.random()

# Display the secret and public keys
print(f"Secret: {keypair.secret}")
print(f"Public Key: {keypair.public_key}")

# Send the public key to the Friendbot (Testnet) to create the account
public_key = keypair.public_key
response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")

# Check if the account was created successfully
if response.status_code == 200:
    print("SUCCESS! You have a new account :)")
    print(response.json())  # Display transaction details
else:
    print("ERROR! Could not create the account.")
