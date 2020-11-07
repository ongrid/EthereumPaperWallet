# Ethereum wallet generator

This script generates Ethereum private key and corresponding address in the following formats:

* Address in hex (EIP-55) and QR
* Etherscan link + QR
* 12-word BIP-44 seed phrase compatible with Metamask (words + QR)
* Private key in hex and QR

## Usage

```sh
python3 -m vernv venv
source ./venv/bin/activate
python generate_wallet.py
```

The key pair and address will be generated and printed to stdout then printable page will appear in your browser.
