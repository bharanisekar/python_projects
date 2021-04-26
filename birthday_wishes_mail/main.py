##################### Extra Hard Starting Project ######################
import smtplib
import random
import datetime as dt
import pandas
import smtplib, ssl

now = dt.datetime.now()
day = now.day
month = now.month
tuples = (day, month)



# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

birthday_dates ={(row.day,row.month):row for (index,row) in data.iterrows()}
name = birthday_dates[tuples]["name"]
email = birthday_dates[tuples]["email"]
if tuples in birthday_dates:
    ran = random.randint(1,3)
    with open(f"letter_templates/letter_{ran}.txt") as file:
        content = file.read()
        mail =content.replace("[NAME]", f"{name}")
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "ksbharani33kick@gmail.com"
        receiver_email = email
        password = "kan33kick"
        message = f"Subject: BirthDay Wishes!!\n\n{mail}"

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


# 4. Send the letter generated in step 3 to that person's email address.
