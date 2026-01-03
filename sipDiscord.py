import discord
import os
import asyncio
import aiohttp

# delete old message

TOKEN = os.getenv("elfak_bot")
CHANNEL_ID = os.getenv("sip_id")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)

    deleted = 0
    async for message in channel.history(limit=None):
        await message.delete()
        deleted += 1

    print(f"Deleted {deleted} messages")
    await client.close()

client.run(TOKEN)

# send new message

WEBHOOK_URL = os.getenv("sip")

class BOTButton(discord.ui.View):
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
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(
            WEBHOOK_URL,
            session=session
        )

        await webhook.send(
            content="@everyone",
            view=BOTButton(),
            file=discord.File("sip.png")
        )

asyncio.run(main())

