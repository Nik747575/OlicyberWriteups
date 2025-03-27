<h1 style="text-align: center;">Flags shop</h1>

<p style="text-align: center; font-size: 16px;">
  <strong>Challenge:</strong> <a href="https://training.olicyber.it/challenges#challenge-43">https://training.olicyber.it/challenges#challenge-43</a>
</p>


<!--<center><img src="https://raw.githubusercontent.com/Nik747575/OlicyberWriteups/main/Fotochallenge/Cagliari.png" alt="Stemma" height="130" width="110.5" ></center>-->



<p style="font-size: 15px;">
  Per questa usiamo <a href="https://portswigger.net/burp/documentation/desktop/getting-started/download-and-install">Burpsuite</a> .<br>
  La challenge ci fornisce un link ad un sito che sembra un' online shop.<br>
  Analizzando il sito notiamo che abbiamo un credito base di 100€ e che ci sono tre articoli, di cui uno però costa 1000€<br>
  Ispezionando il sito possiamo vedere che il credito residuo è salvato in un header, quindi tramite burpsuite possiamo modificare l'header<br>
  <strong>Burp Suite è un software utilizzato per effettuare penetration test sulle applicazioni web.</strong><br>
  Possiamo utilizzare questo software per analizzare le richieste di un sito web e modificare il codice di quest'ultimo.<br>
  Intercettando con Burp Suite il sito datoci dalla challenge, possiamo modificare l'header che contiene il credito residuo, e mandare una richiesta modificata per poter acquistare l'articolo che costa 1000€.
</p>