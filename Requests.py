import requests

class Requests:
    def getText(url, payload={}):
        try:
            r = requests.get(url, params=payload)
            if r.status_code == 200:
                return r.text
        except Exception as e:
            print(e)
        return None
