import sys
import imaplib
import getpass
import email
import email.header
import datetime
import credentials

from dao import Dao

EMAIL_ACCOUNT = credentials.email
EMAIL_PASS = credentials.password
SUBJECT = '(Subject "DevOps")'

def searchMailbox(M):
   # search in mail box.
   rv, filter = M.search(None, SUBJECT)
   if rv != 'OK':
       print "No messages found!"
   return filter

def processMailbox(M):
    # do with the mailbox
   messages = searchMailbox(M)[0].split()

   for num in messages:
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message {}".format(num)
            return
        processMessage(data)

def decodeHeader(data):
    parse = unicode(data)
    #print data
    return parse.replace('"', '')

def processMessage(message):
    # process each message
    msg = email.message_from_string(message[0][1])
    subject = decodeHeader(msg['Subject'])
    name = decodeHeader(msg['FROM'])

    print "Message: {}".format(subject)
    print "Raw Date: {}".format(msg['Date'])
    print "FROM: {}".format(name) 

    # Now convert to local date-time
    date_tuple = email.utils.parsedate_tz(msg['Date'])
    if date_tuple:
        local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        message_date = local_date.strftime("%d-%m-%Y")
        print "Local Date:" + message_date

    d = Dao()
    sentence = "INSERT INTO EMAIL (NAME,SUBJECT,EMAIL) VALUES ('{}','{}','{}')".format(name,subject,message_date)
    d.execute(sentence)


def init():

    d = Dao()
    d.dropTable()
    d.createTable()

    M = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        rv, data = M.login(EMAIL_ACCOUNT, EMAIL_PASS)
    except imaplib.IMAP4.error:
        print "LOGIN FAILED!!! "
        sys.exit(1)

    #print rv, data
    print "Login succesfull"

    rv, mailboxes = M.list()
    if rv == 'OK':
        print "Mailboxes OK"
        #print mailboxes

    rv, data = M.select("INBOX")
    if rv == 'OK':
        print "Processing mailbox...\n"
        processMailbox(M)
        M.close()
    else:
        print "ERROR: Unable to open mailbox ", rv
        M.logout()

init()