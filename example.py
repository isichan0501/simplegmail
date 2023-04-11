from simplegmail import Gmail


import pysnooper
import time
from simplegmail import Gmail
import os
from dotenv import load_dotenv
import datetime
import pathlib
from line_notify import line_push
from util_sheet import get_sheet_with_pd, set_sheet_with_pd, writeSheet
from simplegmail.query import construct_query

load_dotenv(verbose=True)

#get main accountlist
def get_owner():
    owner_account = os.getenv('GMAIL_OWNER')
    owner_list = owner_account.split(',')
    return owner_list

#トークンの絶対パスを取得
@pysnooper.snoop()
def get_gmail_instance(token_name):
    my_secret = os.path.abspath("./token/{}_secret.json".format(token_name))
    my_token = os.path.abspath("./token/{}_token.json".format(token_name))
    gmail = Gmail(my_secret, my_token)
    return gmail


# import pdb;pdb.set_trace()

class MyGmail(Gmail):

    def __init__(self, token_name):
        my_secret = os.path.abspath("./token/{}_secret.json".format(token_name))
        my_token = os.path.abspath("./token/{}_token.json".format(token_name))
        super().__init__(my_secret, my_token)


#@pysnooper.snoop()
def get_send_messages_with_query(gmail, to_email, from_email):
    labels = gmail.list_labels()
    own_label = list(filter(lambda x: x.name == 'own', labels))[0]
    query_params = {
        "newer_than": (1, "month"),
        "recipient": [to_email],
        "sender": [from_email],
        "labels": labels,
        # "exclude_labels": True

    }

    sent_list = gmail.get_messages(query=construct_query(query_params))
    return sent_list




if __name__ == "__main__":

    gmail = MyGmail(token_name="eri")
    messages = gmail.get_messages(query=construct_query(exact_phrase='sibuya1993@gmail.com'))
    import pdb;pdb.set_trace()
    # gmail = get_gmail_instance(token_name="eri")
    messages = gmail.get_unread_inbox()
    # Print them out!
    for message in messages:
        try:
            print("To: " + message.recipient)
            print("From: " + message.sender)
            print("Subject: " + message.subject)
            print("Date: " + message.date)
            print("Preview: " + message.snippet)
            
            print("Message Body: " + message.plain)  # or message.html
        except Exception as e:
            import pdb;pdb.set_trace()
            

        
    import pdb;pdb.set_trace()
    print(gmail)