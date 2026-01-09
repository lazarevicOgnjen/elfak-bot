import discord
import os
import asyncio

TOKEN = os.getenv("elfak_bot")
CHANNEL_ID = int(os.getenv("pj_id"))

intents = discord.Intents.default()

client = discord.Client(intents=intents)


class BOTButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(
            discord.ui.Button(
                label="Forum link",
                url="https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=11&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=",
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
        content="@pj",
        view=BOTButton(),
        file=discord.File("pj.png")
    )

    print("New message sent")

    await client.close()


client.run(TOKEN)
