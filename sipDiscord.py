import discord
import asyncio
import os

WEBHOOK_URL = os.getenv("sip")

class SIPButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(
            discord.ui.Button(
                label="SIP link",
                url="https://sip.elfak.ni.ac.rs/",
                style=discord.ButtonStyle.link
            )
        )

async def main():
    intents = discord.Intents.none()
    client = discord.Client(intents=intents)

    async with client:
        webhook = discord.Webhook.from_url(
            WEBHOOK_URL,
            client=client
        )

        await webhook.send(
            content="@everyone",
            view=SIPButton(),
            file=discord.File("sip.png")
        )

asyncio.run(main())
