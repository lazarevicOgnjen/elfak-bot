import os
from dhooks import Webhook, File

aip_image = "aip.png"

WEBHOOK_URL = os.getenv("aip")
hook = Webhook(WEBHOOK_URL)

file = File(aip_image, name="aip.png")

hook.send(
    "@everyone\n\n"
    "**[website link - click here -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=3&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=)**",
    file=file
)

