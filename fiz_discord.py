import discord
import os
import asyncio

TOKEN = os.getenv("elfak_bot")
CHANNEL_ID = int(os.getenv("fiz_id"))

intents = discord.Intents.default()

client = discord.Client(intents=intents)


class BOTButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(
            discord.ui.Button(
                label="FIZIKA link",
                url="https://mikro.elfak.ni.ac.rs/predmeti/fizika/",
                style=discord.ButtonStyle.link
            )
        )


@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("Channel not found")
        await client.close()
        return

    
    deleted = 0
    async for message in channel.history(limit=None):
        await message.delete()
        deleted += 1
        await asyncio.sleep(0.3)

    print(f"Deleted {deleted} messages")

    
    await channel.send(
        content="@fiz",
        view=BOTButton(),
        file=discord.File("fiz.png")
    )

    print("New message sent")

    await client.close()


client.run(TOKEN)
