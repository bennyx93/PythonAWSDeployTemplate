import re
import time
import logging

from pprint import pprint as pp


def lambda_handler(event, context):

    full_description = "Hello from AWS"
    print full_description
    
# If run interactively from a shell
if __name__ == "__main__":
    ret = lambda_handler(None, None)
    pp(ret)
