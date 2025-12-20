import os
from dhooks import Webhook, Embed, File

lp_image = 'lp.png'

WEBHOOK_URL = [os.getenv('lp')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[website link - click here -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=41&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=)**",
        color=0x3498DB
    )
    
    embed.set_image(url="attachment://lp.png")
    file = File(lp_image, name="lp.png")
    hook.send("@everyone", embed=embed, file=file)
