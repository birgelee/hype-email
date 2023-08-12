aws configure set region us-west-1 --profile default

aws sesv2 create-contact-list --cli-input-json file://contact-list.json

aws sesv2 create-contact --cli-input-json file://contact.json


aws sesv2 list-contacts --no-paginate --cli-input-json file://list-contacts.json

#aws sesv2 delete-contact-list --contact-list-name HYPEContacts
aws ses create-template --cli-input-json file://email-template.json



https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/client/list_contacts.html#