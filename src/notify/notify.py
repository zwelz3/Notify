import os
import smtplib
import socket

from getpass import getpass
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


class Message:
    def __init__(
        self,
        subject="Python Notification",
        body="",
        img=None,
        attachment=None
    ):
        # TODO replace with pathlib
        # build message contents
        self.message = MIMEMultipart()
        self.message['Subject'] = subject  # add in the subject
        self.message.attach(MIMEText(body))  # add body contents

        # check if we have anything given in the img parameter
        if img is not None:
            # if we do, we want to iterate through the images, so let's check that
            # what we have is actually a list
            if type(img) is not list:
                img = [img]  # if it isn't a list, make it one
            # now iterate through our list
            for one_img in img:
                img_data = open(one_img, 'rb').read()  # read the image binary data
                # attach the image data to MIMEMultipart using MIMEImage, we add
                # the given filename use os.basename
                self.message.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

        # we do the same for attachments as we did for images
        if attachment is not None:
            if type(attachment) is not list:
                attachment = [attachment]  # if it isn't a list, make it one

            for one_attachment in attachment:
                with open(one_attachment, 'rb') as f:
                    # read in the attachment using MIMEApplication
                    file = MIMEApplication(
                        f.read(),
                        name=os.path.basename(one_attachment)
                    )
                # here we edit the attached file metadata
                file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
                self.message.attach(file)  # finally, add the attachment to our message object


class Notify:
    def __init__(self, email, server='smtp.gmail.com', port='587'):
        if not email:
            self.email = input("Email:")
        else:
            self.email = email

        try:
            self.smtp = smtplib.SMTP(server, port)
            # handshake
            self.smtp.ehlo()
            # start TLS
            self.smtp.starttls()
            # login to server
            self.smtp.login(email, getpass("Password:"))
        except socket.gaierror:
            print("Network connection error.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # disconnect from the server
        self.smtp.quit()

    def send(self, msg: Message):
        try:
            self.smtp.sendmail(self.email, self.email, msg.message.as_string())
            print("Message sent successfully!")
        except socket.gaierror:
            print("Network connection error. Failed to send message.")
