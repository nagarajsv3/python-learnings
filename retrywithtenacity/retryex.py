import requests
from requests.exceptions import HTTPError, ConnectionError
from tenacity import retry , retry_if_exception_type , stop_after_attempt, stop_after_delay
count = 0
import time

@retry(retry=retry_if_exception_type(Exception), stop=(stop_after_attempt(10) | stop_after_delay(5)))
def make_api_call():
    global count
    print(f"*******************Make API Call ; Attempt = {count}")
    
    count = count+1
    try:
        time.sleep(1)
        response = requests.get("https://weather.com")
        print(response)
    except Exception as e:
        raise Exception("Raising Exception")


make_api_call()