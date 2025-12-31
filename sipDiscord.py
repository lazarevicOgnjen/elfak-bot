import os
from dhooks import Webhook, File

sip_image = 'sip.png'

WEBHOOK_URL = os.getenv("sip")
hook = Webhook(WEBHOOK_URL)

file = File(sip_image, name="sip.png")

hook.send(
    "@everyone  SIP\n\n"
    "[- news forum link -](https://sip.elfak.ni.ac.rs)\n",
    file=file
)
