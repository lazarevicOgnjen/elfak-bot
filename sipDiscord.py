import discord
import os
import asyncio

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
    async with discord.Client(intents=discord.Intents.none()) as client:
        webhook = await discord.Webhook.from_url(
            WEBHOOK_URL,
            client=client
        )

        await webhook.send(
            content="@everyone",
            view=SIPButton(),
            file=discord.File("sip.png")
        )

asyncio.run(main())
