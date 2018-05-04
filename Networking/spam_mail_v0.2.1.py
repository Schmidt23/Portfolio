# ! encoding=utf-8

"""Sends given number of mails to potentially multiple, random recipients from a potentially random sender address.
Default message is the current date and time, subject is number/index of mail."""

import smtplib
from email.mime.text import MIMEText
import random
import sys
import getopt
import time


def spamming_mail(svr, msg_cnt, sndr, smpl_sz, sbj):
    try:
        # connect to SMTP-Server, Port can be named like 'host:port' or 'host',port
        s = smtplib.SMTP(svr)
        # debug for output to console
        s.set_debuglevel(1)

        # content of mail
        if msg_cnt == "time":
            # give current time as message if none is given
            msg_cnt = time.strftime("%a, %d %b %Y %H:%M:%S")
        msg = MIMEText(msg_cnt)

        if sndr == "random":
            # choose random sender from pool if no address is given
            sndr = random.choice(potential_senders)

        # shuffle the list in place incase all elements are used
        random.shuffle(recipients)
        # pick a random sample of n from recipient-list
        rand_recipients = random.sample(recipients, smpl_sz)

        msg['Subject'] = sbj
        msg['From'] = sndr
        msg['To'] = ", ".join(rand_recipients)

        try:
            s.sendmail(sndr, rand_recipients, msg.as_string())
        finally:
            s.quit()
    except Exception as e:
        print e

# pick number of emails and potentially choose subject
if __name__ == "__main__":
    # default values
    server = '127.0.0.1'
    sender = "random"
    msg_content = "time"
    sample_size = 1
    nr_mails = 1

    potential_senders = ['test01.sender@test.me', 'test02.sender@test.me',
                         'test03.sender@test.me', 'test04.sender@test.me',
                         'test05.sender@test.me']

    # pool of potential recipients
    recipients = ['test01.recipient@test.me', 'test02.recipient@test.me',
                  'test03.recipient@test.me', 'test04.recipient@test.me',
                  'test05.recipient@test.me']

    # get sysargs
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:m:a:r:b:n:")
    except getopt.GetoptError:
        print 'script.py -s <server> -m <message> -a <sender> -r <sample_size/nr_recipients> -n <number_mails>'
        sys.exit(2)

    # switch defaults with sysargs
    for opt, arg in opts:
        if opt == '-h':
            print 'spam_mail.py -s <server> -m <message> -a <sender> -r <sample_size/nr_recipients> -n <number_mails>'
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

    for i in xrange(nr_mails):
        # subject counts up with number of mails
        spamming_mail(server, msg_content, sender, sample_size, "%d" % i)
