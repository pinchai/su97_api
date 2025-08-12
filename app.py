from flask import Flask, render_template
from flask_mail import Mail, Message
import requests

app = Flask(__name__)

# Configuration for Gmail SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'e16153937@gmail.com'
app.config['MAIL_PASSWORD'] = 'fpkjrhkbhagffsue'  # Use App Password from Google
app.config['MAIL_DEFAULT_SENDER'] = 'e16153937@gmail.com'
mail = Mail(app)


#Global variable
app.config['IMAGE_DIR'] = '/static/product/'


@app.get('/sendMail')
def send_mail():
    msg = Message('Hello My Love', recipients=['pinchai.pc@gmail.com'])
    msg.body = 'This is a plain text email sent from Flask.'
    message = render_template('mail/invoice.html')
    msg.html = message
    try:
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return f'An error occurred: {str(e)}'

import route

if __name__ == '__main__':
    app.run()
