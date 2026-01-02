import discord
import os

WEBHOOK_URL = os.getenv("sip")

class SIPButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(
            discord.ui.Button(
                label="SIP link",
                url="https://sip.elfak.ni.ac.rs/",
                style=discord.ButtonStyle.link
            )
        )

webhook = discord.SyncWebhook.from_url(WEBHOOK_URL)

webhook.send(
    content="@everyone",
    view=SIPButton(),
    file=discord.File("sip.png")
)
