import datetime as dt
from pandas import *
import random
from twilio.rest import Client

my_num = "YOUR MOBILE NUMBER"
account_sid = "YOUR TWILLIO ACC SID"
auth_token = "YOUR TWILLIO AUTH TOKEN"

today = dt.datetime.now()

tdy_tuple = (today.month, today.day)

birthday_data = read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data.iterrows()}

if tdy_tuple in birthdays_dict:
    birthday_person = birthdays_dict[tdy_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        birthday_person_name = birthday_person["name"]
        contents = contents.replace("[NAME]", birthday_person_name)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp: YOUR TWILLIO VIRTUAL NUMBER",
        body=f"Its {birthday_person_name}'s Birthday Wish them!!!\n\n{contents}",
        to=f"whatsapp:{my_num}"
    )
    print(message.status)

    ""IF YOU WANT TO STRAIGHT AWAY SEND AN EMAIL TO THE BIRTHDAY PERSON USE THIS CODE...AND REMEBER TO ADD THEIR EMAILS TO THE CSV""
    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     receivers_email = birthday_person["email"]
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(from_addr=my_email,
    #                         to_addrs=receivers_email,
    #                         msg=f"Subject: Happy Birthday!\n\n{contents}")


