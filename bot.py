import os
from dhooks import Webhook

WEBHOOK_URL = [os.getenv('bot')]
for url in WEBHOOK_URL:
    hook = Webhook(url)
    hook.send("@everyone I godina

uur - uvod u racunarstvo
aip - algoritmi i programiranje

II godina RI

bp - baze podataka
oop - objektno orijentisano programiranje
oopj - objektno orijentisano projektovanje
pj - programski jezici
dmat - diskretna matematika
lp - logicko projektovanje
sp - strukture podataka

II godina

os - operativno sistemi
rm - racunarske mreze
ti - teorija igara")
