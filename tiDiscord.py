import os
from dhooks import Webhook, Embed, File

ti_image = 'ti.png'

WEBHOOK_URL = [os.getenv('ti')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[website link - click here -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=110&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=)**",
        color=0x3498DB
    )
    
    embed.set_image(url="attachment://ti.png")
    file = File(ti_image, name="ti.png")
    hook.send("@everyone", embed=embed, file=file)
