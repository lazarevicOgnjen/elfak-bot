import os
from dhooks import Webhook, File

pj_image = 'pj.png'

WEBHOOK_URL = os.getenv("pj")
hook = Webhook(WEBHOOK_URL)

file = File(pj_image, name="pj.png")

hook.send(
    "@everyone PJ\n"
    "[- forum post link -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=11&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=)",
    file=file
)
