# Notify
A basic package for sending email messages from python via SMTP. 

## Install
* Download from git
* `pip install -e .`

## Basic Usage
```python
from notify import Notify, Message

msg = Message(subject="Test", body="Text")
with Notify("example.email@gmail.com") as ntfy:
    ntfy.send(msg)
```

## Other SMTP options
| Provider | Server Address | Port (TLS) |
| :--------: | :-----------: | :--------: |
| Outlook | smtp-mail.outlook.com | 587 |
| Gmail | smtp.gmail.com | 587 |
| Yahoo | smtp.mail.yahoo.com | 587 |
