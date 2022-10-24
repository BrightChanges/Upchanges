from itsdangerous import URLSafeTimedSerializer
from Upchanges import app, mail, Message, MAIL_USERNAME

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def send_email(subject, recipients, html):
    msg = Message(subject, sender=MAIL_USERNAME, recipients=recipients)
    msg.html = html
    mail.send(msg)