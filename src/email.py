#encoding:utf8
from flask_mail import Message
from flask import render_template, current_app
from src import mail

def send_email(to, subject, template, user, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.html = render_template(template + '.html', **kwargs,user=user)
    # msg.body = render_template(template + '.txt', **kwargs,user=user)
    mail.send(msg)
