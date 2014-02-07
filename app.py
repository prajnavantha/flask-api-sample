"""
app.py
~~~~~~

A simple API service which only allows authenticated developers to make API
requests.

To run this sample, you need a couple of things:

    1. A Stormpath account: http://stormpath.com/
    2. You need to set the following two environment variables:
    STORMPATH_API_KEY_ID and STORMPATH_API_KEY_SECRET (with the appropriate
    values).
    3. You need to create a Stormpath application named 'flask-api-sample',
    along with the automatically created directory.
    4. You need to manually create at least one user account in the
    'flask-api-sample' application (for testing)!

Once you have the above things ready, you can bootstrap this project quite
easily:

    ```bash
    $ pip install -U flask stormpath
    $ python app.py
    ```

This will install all of the required Python packaged, and run the API service
locally.
To test out the API service, you can use cURL locally:

    ```bash
    $ curl -v 'http://localhost:5000'
    $ curl -v --user '<your_username_or_email_address>:<your_password>' 'http://localhost:5000'
    ```

The first example above will cause you to get a 401 UNAUTHORIZED response from
the server (since you have not specified any valid credentials).

Assuming you put the proper credentials in the second example, you should be
able to authenticate to the API and get back a valid response!
"""


from os import environ
from sys import exit

from flask import Flask, jsonify, request
from stormpath.client import Client


##### GLOBALS
app = Flask(__name__)

try:
    stormpath_app = Client(
        id = environ.get('STORMPATH_API_KEY_ID'),
        secret = environ.get('STORMPATH_API_KEY_SECRET'),
    ).applications.search('flask-api-sample')[0]
except:
    print "Error! Couldn't find the Stormpath application."
    exit(1)


##### API
@app.route('/')
def api():
    """Simple API endpoint which requires user authention to access.

    Users can access this endpoint by using HTTP Basic Authentication when
    making their HTTP request to the service.

    We'll then use Stormpath's API to authenticate the user securely.

    If the user cannot be authenticated we'll return a JSON error message along
    with a 401 UNAUTHORIZED status code.

    If the user can be authenticated successfully, we'll return a JSON message
    along with a 200 OK status code.
    """
    if not request.authorization:
        return jsonify({'error': 'Username and password required.'}), 401

    try:
        stormpath_app.authenticate_account(
            request.authorization.username,
            request.authorization.password,
        )
    except:
        return jsonify({'error': 'Incorrect username or password.'}), 401

    return jsonify({'status': 'Successfully authenticated with Stormpath!'})


if __name__ == '__main__':
    app.run()
