import discord
import os
import asyncio
import aiohttp

WEBHOOK_URL = os.getenv("ti")

class BOTButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(
            discord.ui.Button(
                label="Forum link",
                url="https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=110&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=",
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
            file=discord.File("ti.png")
        )

asyncio.run(main())
