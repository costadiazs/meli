from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dao import Dao

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    d = Dao()
    d.dropTable()
    d.createTable()
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    response = service.users().messages().list(userId='me',
                                               q='DevOps').execute()
    #print(messages)

    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])
    for msg in messages:
        GetMessages(service, msg['id'])

    #print(msg['id'])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
            
def GetReplace (msg):
    print(msg[0])
    return msg.replace("['", '').replace("]'", '')

def GetMessages (service, msg_id):
    #message = service.users().messages().get(userId="me", id=msg_id).execute()
    #print (message)
    messageheader = service.users().messages().get(userId="me", id=msg_id,
                                             format="full", metadataHeaders=None).execute()
    # print(messageheader)
    message = messageheader["snippet"]
    headers=messageheader["payload"]["headers"]
    
    subject= [i['value'] for i in headers if i["name"]=="Subject"]
    yfrom= [i['value'] for i in headers if i["name"]=="From"]

    # message = GetReplace(message)
    # yfrom = GetReplace(yfrom)
    # subject = GetReplace(subject)
    
    #print(subject[0])
    #print(message)
    d = Dao()
    sentence = "INSERT INTO EMAIL (NAME,SUBJECT,EMAIL) VALUES ('{}','{}','{}')".format(yfrom[0],subject[0],message)
    print(sentence)
    d.execute(sentence)
    
    
if __name__ == '__main__':
    main()