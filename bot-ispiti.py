import os
from dhooks import Webhook

WEBHOOK_URL = [os.getenv('bot')]
for url in WEBHOOK_URL:
    hook = Webhook(url)
    hook.send("""@everyone krenula je prijava ispita !""")
