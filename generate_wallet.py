#!/usr/bin/env python3
BLOCK_EXPLORER_URL = "https://etherscan.io/address/"
import webbrowser
import os
from jinja2 import Environment, FileSystemLoader
from coincurve import PrivateKey
from eth_keys import keys
from os import urandom
from eth_hash.auto import keccak
import base64
import qrcode
import qrcode.image.svg
import six
from mnemonic import Mnemonic
from bip44 import Wallet
from bip44.utils import get_eth_addr

def generate_qrcode(string, size=128):
    stream = six.BytesIO()
    qrcode.make(string, image_factory=qrcode.image.svg.SvgImage, box_size=10).save(stream)
    b64_image_string = base64.b64encode(stream.getvalue()).decode('utf-8')
    return f"<img  width='128' src='data:image/svg+xml;base64,{ b64_image_string }'>"

mnemo = Mnemonic("english")
words = mnemo.generate()
w = Wallet(words)
sk, pk = w.derive_account("eth", account=0)

print("CS address: %s" % get_eth_addr(pk))
print("Private key in hex format: %s" % sk.hex())
addr = get_eth_addr(pk)
addr_qr = generate_qrcode(addr)

words_qr = generate_qrcode(words)

url = BLOCK_EXPLORER_URL + addr
url_qr = generate_qrcode(url)
sk_qr = generate_qrcode(sk.hex())
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('template.html')
html = template.render(words=words, words_qr=words_qr, addr=addr, addr_qr=addr_qr, url=url, url_qr=url_qr, sk_hex=sk.hex(), sk_qr=sk_qr)
webbrowser.open_new_tab("data:text/html;base64," + base64.b64encode(html.encode()).decode())