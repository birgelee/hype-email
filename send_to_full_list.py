#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import json
import datetime
import time
import random
import os
import email_contents_object
import boto3

def parse_args():
    parser = argparse.ArgumentParser()
    # This is a CAIDA AS topology.
    parser.add_argument("-u", "--users_csv",
                        default="./hype-email-list.csv")
    return parser.parse_args()

def get_current_human_time():
    value = datetime.datetime.fromtimestamp(time.time())
    return value.astimezone(datetime.timezone.utc).strftime('UTC %Y-%m-%d %H:%M:%S')


def run_cmd(cmdAndArgsList):
    #print(cmdAndArgsList)
    retryCount = 1
    out = b''
    err = b''
    for i in range(retryCount):
        p = subprocess.Popen(cmdAndArgsList, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if err == b'':
            return out.decode('utf-8')
        elif "kex_exchange_identification" in err.decode('utf-8'): # Just try again in this case.
            continue
        else:
            # Assume this is an ssh connection error.
            print(f"[{get_current_human_time()}] stderr: \"{err.decode('utf-8')}\" from cmd {cmdAndArgsList}") # This could go to stderr or stdio.
            raise IOError(f"Non-empty error: {err.decode('utf-8')}, stdout: {out.decode('utf-8')}")
            return out.decode('utf-8')
        #pass
        #
    print(f"[{get_current_human_time()}] Max retries ({retryCount}) reached. stderr: \"{err.decode('utf-8')}\" from cmd {cmdAndArgsList}") # This could go to stderr or stdio.
    return out.decode('utf-8')



def main(args):
    #nextToken = " AYADeCiOH2b5Hew/Y73mk3ng7gcAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREE0N3JiOE5QQ0dFbUZFcmtnWDExQWo4OGYvSjVBMlFHMVJ5N2o4cU5LNnlndXFxVDV4bnhYYnNGYlNoNzg2ZW8ydz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMTo4Mjc1NzgwMzM4Njc6a2V5L2VmYjllMDA2LTFlYjMtNGFkZi05MjJiLWJmODkzYjk0MzhjNwC4AQIBAHjLB4/2FF61wyZF95iFLBZyyHwgT1kWWNscr7BfQ4blRQHQL+fMuDUyNCC48drb8iJ3AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM6ES+r8uxTHNte6pWAgEQgDsrQBK4Nkx0BF+eUOcsJ2nZSXSS3lMJWgfKtYnYhROAlXQww1awRamhpWswXN+XuL2yVe8n134okC5P6wIAAAAADAAAEAAAAAAAAAAAAAAAAAB85q74nz5KXEatqiB8AL8Q/////wAAAAEAAAAAAAAAAAAAAAEAAABxUcbBw/w6o5ZtKuvHek0UtjF9gOgYst+lWCMPkNyfr6UHY/Sd+ZutFLQRo2NS2rpsYbDAoekYgfU/Bmy9xUeHsFVOEcow2qTttQvCEXOJrL9me8KN7FWlUE0pnN+6O9ej9GUeOuCq3zBAqlZXKPCq1VRd+n9iu9j0TXdWCgUHg9LMAGcwZQIxALaJ7utZI/q3LyvBAnRKW9g8KQbcq/gaN/DJWfsjUAOLF4KYiS8kYzL9VKQtXrTCFgIwGkk45d47vmazyz0DpjP2cF1Ri854LOE0zhN737fNWa9w46slc+mMOBE7ZN6FSXUj"
    emailListJson = json.loads(run_cmd(["aws", "sesv2", "list-contacts", "--cli-input-json", "file://list-contacts.json"]))
    #print(json.dumps(email_contents_object.emailContentsObject))
    client = boto3.client('sesv2')
    while True:
        for contact in emailListJson['Contacts']:
            response = client.send_email(
                FromEmailAddress='events@gethype.live',
                Destination={
                    'ToAddresses': [
                        contact['EmailAddress']
                    ]
                },
                Content=email_contents_object.emailContentsObject,
                ListManagementOptions={
                    'ContactListName': 'HYPEContacts',
                    'TopicName': 'News'
                }
            )
            print(f"Emailed {contact['EmailAddress']}")
        if "NextToken" not in emailListJson:
            break
        nextToken = emailListJson['NextToken']
        emailListJson = json.loads(run_cmd(["aws", "sesv2", "list-contacts", "--next-token", nextToken, "--cli-input-json", "file://list-contacts.json"]))
        print("Paginating")





if __name__ == '__main__':
    main(parse_args())

