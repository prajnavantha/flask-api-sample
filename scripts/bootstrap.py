"""
boostrap.py
~~~~~~~~~~~

Bootstrap this demo application.

This will create a new Stormpath application for you named 'flask-api-sample',
and provision a new developer account for your new application.

This example shows you how to securely create new Stormpath users, and
provision API keys for these users.
"""


from os import environ
from sys import exit
from uuid import uuid4

from stormpath.client import Client


##### GLOBALS
client = Client(
    id = environ.get('STORMPATH_API_KEY_ID'),
    secret = environ.get('STORMPATH_API_KEY_SECRET'),
)

try:
    application = client.applications.create({
        'name': 'flask-api-sample',
        'description': 'Flask API sample application.',
    }, create_directory=True)
except:
    print "Error: application flask-api-sample already exists!"
    exit(1)


# Create a new user.
user = application.accounts.create({
    'given_name': 'demo',
    'surname': 'user',
    'email': 'demo@user.com',
    'password': 'someSECRETp4ssw0rd!',
})


# Generate an API key for this user.
#
# This is a list as you typically want to allow users to have more than one API
# key at a time.  This way you can securely cycle API keys without downtime.
user.custom_data['api_keys'] = [uuid4().hex]
user.save()


print 'User Details'
print '------------'
print 'First Name:', user.given_name
print 'Last Name:', user.surname
print 'Email:', user.email
print 'API Key:', user.custom_data['api_keys'][0]
