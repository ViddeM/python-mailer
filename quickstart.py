from __future__ import print_function

import base64
import os.path
import pickle
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.send", "https://www.googleapis.com/auth/gmail.modify",
          "https://www.googleapis.com/auth/gmail.compose", "https://www.googleapis.com/auth/gmail.settings.sharing"]

service = None

def main():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    global service
    service = build("gmail", "v1", credentials=creds)

    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
        print("No labels found.")
    else:
        print("Labels:")
        for label in labels:
            print(label["name"])


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_formatted_message(message):
    try:
        message = service.users().messages().send(userId="me", body=message).execute()
        print("Message Id: %s" % message["id"])
        return message
    except HttpError as error:
        print("An error occured: %s" % error)

def send_message(sender, to, subject, message_text):
    send_formatted_message(create_message(sender, to, subject, message_text))
