#! -*- coding: utf-8 -*-

"""Sends given number of mails to potentially multiple, random recipients from a potentially random sender address.
Default message is the current date and time, subject is number/index of mail.
Thanks to https://docs.python.org/2.7/ and stackoverflow.com for most of the blueprints."""

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from os.path import basename
import mimetypes
import random
import sys
import getopt
import time


def spamming_mail(svr, msg_cnt, sndr, smpl_sz, sbj, att, dl):

    try:
        # connect to SMTP-Server, Port can be named like 'host:port' or 'host',port
        s = smtplib.SMTP(svr)
        # debug for output to console
        if dl != 1:
            s.set_debuglevel(dl)

        msg = MIMEMultipart()
        # content of mail
        if msg_cnt == "time":
            # give current time as message if none is given
            msg_cnt = time.strftime("%a, %d %b %Y %H:%M:%S")
        msg.attach(MIMEText(msg_cnt))

        if sndr == "random":
            # choose random sender from pool if no address is given
            sndr = random.choice(potential_senders)

        # shuffle the list in place in case all elements are used
        random.shuffle(recipients)
        # pick a random sample of n from recipient-list
        rand_recipients = random.sample(recipients, smpl_sz)

        msg['Subject'] = sbj
        msg['From'] = sndr
        msg['To'] = ", ".join(rand_recipients)
        msg['Date'] = time.strftime("%a, %d %b %Y %H:%M:%S")

        # guess the mimetype and attach to mail.
        if att:
            print "Attachments: ", att
            for f in att:
                ctype, encoding = mimetypes.guess_type(f)
                if ctype is None or encoding is not None:
                    #  If type could not be guessed, use a generic Base type.
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                if maintype == 'text':
                    with open(f, "rb") as fl:
                        part = MIMEText(fl.read(), _subtype=subtype)
                elif maintype == 'image':
                    with open(f, "rb") as fl:
                        part = MIMEImage(fl.read(), _subtype=subtype)
                elif maintype == 'audio':
                    with open(f, "rb") as fl:
                        part = MIMEAudio(fl.read(), _subtype=subtype)
                else:
                    with open(f, "rb") as fl:
                        part = MIMEBase(maintype, subtype)
                        part.set_payload(fl.read())
                    encoders.encode_base64(part)
                part['Content-Disposition'] = 'attachment; filename="%s  "' % basename(f)
                # attach to message
                msg.attach(part)

        try:
            s.sendmail(sndr, rand_recipients, msg.as_string())
        finally:
            s.quit()
    except Exception as e:
        print e

    if dl > 0:
        print "Sending Mail nr. %d, FROM: %s TO: %s" % (int(sbj)+1, sndr, ", ".join(rand_recipients))


# pick number of emails and potentially choose subject
if __name__ == "__main__":
    # default values
    server = '127.0.0.1'
    sender = "random"
    msg_content = "time"
    sample_size = 1
    nr_mails = 1
    attachments = []
    debuglevel = 0

    potential_senders = ['test01.sender@test.me', 'test02.sender@test.me',
                         'test03.sender@test.me', 'test04.sender@test.me',
                         'test05.sender@test.me']

    # pool of potential recipients
    recipients = ['test01.recipient@test.me', 'test02.recipient@test.me',
                  'test03.recipient@test.me', 'test04.recipient@test.me',
                  'test05.recipient@test.me']

    # get sysargs
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:m:a:r:b:n:f:d:")
    except getopt.GetoptError:
        print 'spam_mail.py -s <server> -m <message> -a <sender> -r <sample_size/nr_recipients> -n <number_mails> -f ' \
              '<file> -d <debuglevel; 1 | 0>'
        sys.exit(2)

    # switch defaults with sysargs
    for opt, arg in opts:
        if opt == '-h':
            print 'spam_mail.py -s <server> -m <message> -a <sender> -r <sample_size/nr_recipients> -n <number_mails>' \
                  '-f <file> -d <debuglevel;0-2>'
            sys.exit()
        elif opt == '-s':
            server = arg
            print "server: ", server
        elif opt == '-m':
            msg_content = arg
            print "message: ", msg_content
        elif opt == '-a':
            # random_sender = False
            sender = arg
            print "sender: ", sender
        elif opt == '-r':
            sample_size = int(arg)
            print "sample_size: ", sample_size
        elif opt == '-n':
            nr_mails = int(arg)
            print "number of mails: ", nr_mails
        elif opt == '-f':
            attachments.append(arg)
        elif opt == '-d':
            debuglevel = int(arg)
            print "debuglevel: ", debuglevel

    for i in xrange(nr_mails):
        # subject counts up with number of mails
        spamming_mail(server, msg_content, sender, sample_size, "%d" % i, attachments, debuglevel)

