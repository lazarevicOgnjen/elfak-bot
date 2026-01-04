import os
from dhooks import Webhook

WEBHOOK_URL = [os.getenv('bot')]
for url in WEBHOOK_URL:
    hook = Webhook(url)
    hook.send("""@everyone 
Ukoliko želite da prestanete da pratite određene predmete, potrebno je da ih u novoj listi predmeta prvo ponovo čekirate, a zatim da ih odčekirate.""")
