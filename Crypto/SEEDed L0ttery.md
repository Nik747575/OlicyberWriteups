<h1 style="text-align: center;">SEEDed L0ttery</h1>

<p style="text-align: center; font-size: 16px;">
  <strong>Challenge:</strong> <a href="https://training.olicyber.it/challenges#challenge-534">https://training.olicyber.it/challenges#challenge-534</a>
</p>

<p style="font-size: 15px;">
  La challenge ci presenta un sito con 2 menù:
</p>

<ul style="font-size: 15px;">
  <li><code>Home</code></li>
  <li><code>Source</code></li>
</ul>

<p style="font-size: 15px;">
  Nel menù <strong>Home</strong>, troviamo una casella dove inserire un numero che verrà utilizzato per criptare la flag.<br>
  Nel menù <strong>Source</strong>, invece, troviamo il codice che viene utilizzato per criptare la flag.<br>
  Esaminando il codice, notiamo la funzione <code>encrypt</code> che utilizza un algoritmo XOR con una chiave generata casualmente a partire da un seed numerico.<br>  
  La chiave segreta viene generata con <code>random.seed(seed)</code>, quindi se conosciamo il seed, possiamo ricreare la stessa chiave.<br>
  Prendendo come esempio il numero <code>23</code>, possiamo rigenerare la stessa chiave per poi fare XOR inverso.
</p>

<h2 style="font-size: 20px;">SOLVE:</h2>

<pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-size: 14px; overflow-x: auto;">
<code class="language-python">import random, binascii

def xor(key, data):
    res = bytearray()
    for i in range(len(data)):
        res.append(data[i] ^ key[i % len(key)])
    return res

def decrypt(seed, encrypted_hex):
    random.seed(seed)
    key = random.getrandbits(32).to_bytes(4, "big")
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    return xor(key, encrypted_bytes).decode()

seed = 23
ciphertext = "8aaf996b9790cb69889cc97fb38dc878b3f69753bef79668dcaea7388af49d5eb382c93dcdbe"
print("FLAG:", decrypt(seed, ciphertext))
</code>
</pre>
