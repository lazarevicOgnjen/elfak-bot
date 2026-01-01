import os
from dhooks import Webhook, File, Embed

sip_image = 'sip.png'

embed = Embed(
    title="🔗 NEWS FORUM",
    url="https://sip.elfak.ni.ac.rs",
    color=0x2F3136
)

WEBHOOK_URL = os.getenv("sip")
hook = Webhook(WEBHOOK_URL)

file = File(sip_image, name="sip.png")

hook.send(
    "@everyone  📢 SIP\n\n",
    embed=embed,
    file=file
)
