import requests

URL = "https://www.mockaroo.com/"

def fetch_net():
    response = requests.get(URL)
    if response.status_code == 200:
        return "abc"
    return "unknown"

def bob_net():
    response = requests.get(URL)
    if response.status_code == 200:
        return "xyz"
    return "unknown"

def parse():
    ans = fetch_net() + " ----"
    ans = ans + bob_net()
    return ans

print(parse())


    
    