# import smtplib
import smtplib, ssl
#
# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "ksbharani33kick@gmail.com"
# receiver_email = "im.bharani.18@gmail.com"
# password = "kan33kick"
# message = """\
# Subject: Birthday Wishes
#
# HAPPY BIRTHDAY DIMPLE."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

# import datetime as dt
#
# now = dt.datetime.now()
# print(now.day, now.month, now.year, now.time(), now.weekday(), now.isoweekday())
# date_of_birth = dt.datetime(year=1997, month=10, day=18,hour=12)
# print(date_of_birth)

import random
import datetime as dt
l=[]
with open("quotes.txt") as file:
    for i in file.readlines():
        l.append(i)
ran =random.choice(l)

thursday = dt.datetime.now()
# print(thursday.isoweekday())
if thursday.isoweekday() == 4:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "ksbharani33kick@gmail.com"
    receiver_email = "im.bharani.18@gmail.com"
    password = "kan33kick"
    message = f"Subject: Motivation\n\n{ran}"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
else:
    print("hii")












