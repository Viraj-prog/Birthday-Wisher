
from pandas import *
import datetime as dt
from random import randint
import smtplib



data = read_csv("birthdays.csv")
now = dt.datetime.now()
current_day = now.day
current_month = now.month

data= data.to_dict("records")
birthday = False
for row in data:
    if row['day'] == current_day and row['month'] == current_month:
        birthday = True
        email = row['email']
        name = row['name']

        with open(f"letter_{randint(1,3)}.txt",'r') as file:
            letter = file.read()
            letter = letter.replace("[NAME]",name)
            letter = letter.replace("Angela","Viraj")

        my_email = "viraj.practice99@gmail.com"
        password = "qspu aihq wfun vjep"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=email,
                                msg=f"Subject:HAPPY BIRTHDAY!\n\n{letter}")


