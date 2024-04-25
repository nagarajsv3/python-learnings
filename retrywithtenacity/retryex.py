import requests
from requests.exceptions import HTTPError, ConnectionError
#from tenacity import retry , retry_if_exception_type , stop_after_attempt, stop_after_delay
from tenacity import *

import time
import datetime
#
#stop_after_attempt(10) - stops after 10 attempts
#stop_after_delay(5) - stops after 5 seconds

count = 0
#@retry(retry=retry_if_exception_type(Exception), stop=(stop_after_attempt(10) | stop_after_delay(5)))
#@retry(wait=wait_fixed(2)) #retries after 2 seconds
@retry(retry=retry_if_exception_type(Exception), stop=(stop_after_attempt(10) | stop_after_delay(5)), wait=wait_fixed(2))
def make_api_call():
    global count
    print(f"*******************Make API Call ; Attempt = {count}")
    
    count = count+1
    try:
        time.sleep(1)
        response = requests.get("https://weather.com1")
        print(response)
    except Exception as e:
        raise Exception("Raising Exception")
    
@retry(wait = wait_exponential(multiplier=1, max=10))    
def exponential_backoff_attempt():
    print('runs at seconds intervals of 0, 2, 4, 8, 10, 10, 10')
    
    print(datetime.datetime.now())
    raise Exception


#make_api_call()
exponential_backoff_attempt()