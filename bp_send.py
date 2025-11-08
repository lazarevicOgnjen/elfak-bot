import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# --- Configuration ---
SENDER_EMAIL = os.getenv("BOT_MAIL")
SENDER_PASSWORD = os.getenv("BOT_PASS")
SMTP_SERVER, SMTP_PORT = "smtp.gmail.com", 587
TO_EMAIL = "bp-elfak@googlegroups.com"
IMAGE_PATH = "sip.png"

HTML_BODY = """
<html><body>
<p><img src="cid:embedded_image" style="width:300px;border-radius:10px;"></p>
<p>BP forum -> <a href="https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=4&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2023&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=">link</a></p>
</body></html>
"""

# --- Build the message ---
msg = MIMEMultipart("related")
msg["From"] = SENDER_EMAIL
msg["To"] = TO_EMAIL
msg["Subject"] = "🎓 BP"

alt = MIMEMultipart("alternative")
msg.attach(alt)
alt.attach(MIMEText(HTML_BODY, "html"))

# Attach image if available
try:
    with open(IMAGE_PATH, "rb") as img:
        mime_img = MIMEImage(img.read())
        mime_img.add_header("Content-ID", "<embedded_image>")
        msg.attach(mime_img)
except FileNotFoundError:
    print("⚠️ Image not found, sending email without image.")

# --- Send the email ---
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    print(f"✅ Sent to {TO_EMAIL}")
