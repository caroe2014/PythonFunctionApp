"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
import requests
from requests.exceptions import HTTPError

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

for url in ['https://v-edcaropythonfastapi.azurewebsites.net/users', 'https://v-edcaropythonfastapi.azurewebsites.net/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


