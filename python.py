from numpy import number
import os
import json

from credentials import credentials
from twilio.rest import Client

account_sid = credentials()['account']
auth_token  = credentials()['token']

def number_lookup(number):
    client = Client(account_sid, auth_token)
    phone_number = client.lookups \
                     .v1 \
                     .phone_numbers(number) \
                     .fetch(country_code='US', type=['carrier' ,'caller-name'])

    lookup_result = {
        'carrier' : phone_number.carrier['name'],
        'person' : phone_number.caller_name['caller_name'],
        'number': phone_number.phone_number
    }
    
    return lookup_result

print(number_lookup(''))