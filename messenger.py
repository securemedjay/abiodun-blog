import smtplib

sender_email = "securemedjay@yahoo.com"
password = "maqtgprjkxbmimrc"
receiver_email = "ajibolabiodun@gmail.com"


class Messenger:
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def send_message(self):
        msg = "\r\n".join([
            "Subject: Message From My Website",
            "",
            f"Hello Abiodun,\n\nYou have received the following message from your website\n\nName: {self.name}\n"
            f"Email: {self.email}\n"f"Subject: {self.subject}\nMessage: {self.message}\nSent from my website"
        ])
        with smtplib.SMTP_SSL(host="smtp.mail.yahoo.com", port=465) as connection:
            connection.ehlo()
            # connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=msg)
