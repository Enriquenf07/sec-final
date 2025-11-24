import yagmail
import os
database_url = os.getenv("DATABASE_URL")
email_user = os.getenv("EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")



def send_email(to, subject, contents):
    yag = yagmail.SMTP(email_user, email_password)
    yag.send(
        to=to,
        subject=subject,
        contents=contents,
    )