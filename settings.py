import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
token = os.getenv("SLACK_TOKEN")

def getToken():
    return token