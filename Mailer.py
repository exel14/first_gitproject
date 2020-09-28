import sendgrid
from sendgrid import Mail,Email,Content
sendgrid_api_key = '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'
SUBJECT = 'Hellow'
sg = sendgrid.SendGridAPIClient(sendgrid_api_key)
def sendgrid_email(email,name):
    body = 'Hi,' +name
    message = Mail(
        from_email='showmetheway220@gmail.com',
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=body)
    response = sg.send(message)
sendgrid_email('showmetheway220@gmail.com','eXeL')

