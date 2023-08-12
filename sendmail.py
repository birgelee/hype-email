#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3
client = boto3.client('sesv2')
response = client.send_email(
    FromEmailAddress='events@gethype.live',
    Destination={
        'ToAddresses': [
            'henrybirgelee@gmail.com'
        ]
    },
    #ReplyToAddresses=[
    #    'string',
    #],
    #FeedbackForwardingEmailAddress='admin@gethype.live',
    Content={
        'Simple': {
            'Subject': {
                'Data': 'HYPE Night Live 2 Tomorrow!',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': 'Celebrate at HYPE Night Live 2 tomorrow August 12th! RSVP here: https://www.eventbrite.com/e/hype-night-live-2-tickets-693803112787?utm-campaign=social&utm-content=attendeeshare&utm-medium=discovery&utm-term=listing&utm-source=wsa&aff=ebdsshwebmobile Please visit this URL if you wish to unsubscribe: {{amazonSESUnsubscribeUrl}}',
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': '<h2>Celebrate at HYPE Night Live 2 tomorrow August 12th!</h2> <img src="https://gethype.live/assets/media/hnl2.jpg" alt="HYPE Night Live 2 Poster" width=445 height=445> <br /><h3><a href="https://www.eventbrite.com/e/hype-night-live-2-tickets-693803112787?utm-campaign=social&utm-content=attendeeshare&utm-medium=discovery&utm-term=listing&utm-source=wsa&aff=ebdsshwebmobile">Click here to RSVP!</a><br /> <br /><br /> <br /><p>If you wish to stop recieving these emails please click <a href="{{amazonSESUnsubscribeUrl}}">here to unsubscribe</a></p>',
                    'Charset': 'UTF-8'
                }
            }
        }
        #'Raw': {
        #    'Data': b'bytes'
        #},
        #'Template': {
        #    'TemplateName': 'string',
        #    'TemplateArn': 'string',
        #    'TemplateData': 'string'
        #}
    },
    #EmailTags=[
    #    {
    #        'Name': 'marketing',
    #        'Value': 'news'
    #    },
    #],
    #ConfigurationSetName='string',
    ListManagementOptions={
        'ContactListName': 'HYPEContacts',
        'TopicName': 'News'
    }
)





#response = client.send_email(
#    #Destination={
#    #    'ToAddresses': [
#    #        'henrybirgelee@gmail.com'
#    #    ],
#    #},
#    ListManagementOptions={
#        'ContactListName': 'HYPEContacts',
#        'TopicName': 'News'
#    },
#    Message={
#        'Body': {
#            'Html': {
#                'Charset': 'UTF-8',
#                'Data': '<h1>Hello World</h1><p>This is a pretty mail with HTML formatting</p>',
#            },
#            'Text': {
#                'Charset': 'UTF-8',
#                'Data': 'This is for those who cannot read HTML.',
#            },
#        },
#        'Subject': {
#            'Charset': 'UTF-8',
#            'Data': 'Hello World',
#        },
#    },
#    Source='events@gethype.live',
#)#