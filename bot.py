import os
from dhooks import Webhook, Embed, File

WEBHOOK_URL = [os.getenv('bot')]
for url in WEBHOOK_URL:
    hook = Webhook(url)
    hook.send("@everyone sa strane imate opciju 'Channels & Roles', idete 'Channels & Roles' > 'Customise' tu imate drop-down u kome mozete izabrati predmete za koje zelite da dobijate obavestenja", embed=embed, file=file)
