# 🌌 Stellar Wallet Generator

A simple Python script to generate a Stellar wallet using the `stellar_sdk`. This script creates a keypair with a public and private key, then registers the account on the Stellar Testnet by requesting funds from the Friendbot service.

## ✨ Features

- Generate a new Stellar keypair (public and private keys)
- Create a Testnet account by interacting with the Stellar Friendbot service
- Display transaction details after account creation

## 🚀 Getting Started

### Prerequisites

Ensure Python is installed on your machine. You can download it [here](https://www.python.org/downloads/).

Additionally, install the following Python libraries:

- `stellar_sdk`
- `requests`

Use the following command to install them:

```bash
pip install stellar-sdk requests
```

### 🔧 How to Run the Code

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/stellar-wallet-generator.git
   ```

2. **Navigate to the project folder**:

   ```bash
   cd stellar-wallet-generator
   ```

3. **Run the Python script**:

   ```bash
   python stellar_wallet.py
   ```

## 📝 Code Explanation

Here's a breakdown of what the script does:

### 1. Generate a Keypair

This generates a random keypair with a secret key and public key.

```python
pair = Keypair.random()
```

### 2. Display the Secret and Public Key

Print both the private (secret) key and public key. **Keep your private key safe!** If someone else gains access to it, they will control your wallet.

```python
print(f"Secret: {pair.secret}")
print(f"Public Key: {pair.public_key}")
```

### 3. Request Funds from Friendbot

The Friendbot service gives free XLM on the Stellar Testnet to help developers test their applications.

```python
public_key = pair.public_key
response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
```

### 4. Check if the Account was Created

If the account is successfully created, the script prints a success message along with transaction details. If not, an error message is displayed.

```python
if response.status_code == 200:
    print("SUCCESS! You have a new account :)")
    print(response.json())  # Display transaction details
else:
    print("Error! Could not create account.")
```

## 📈 Example Output

```
Secret: SBH...DPU
Public Key: GCV...T3Q
SUCCESS! You have a new account :)
{
    "_links": { ... },
    "hash": "8cde...b2",
    "ledger": 123456,
    "created_at": "2024-10-29T18:00:00Z",
    "source_account": "GCV...T3Q",
    "successful": true
}
```

## 🛠 Notes

- This script interacts with the **Stellar Testnet**, which is separate from the Mainnet. You can use it to test your Stellar-based applications without risking real funds.
- The Friendbot service only works on the **Testnet**. If you wish to use this on the Mainnet, you’ll need to fund your wallet manually.

---

Happy coding and exploring the Stellar network! 💫
```
