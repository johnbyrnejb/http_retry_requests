import requests


url = 'https://httpstat.us/200'

r = requests.get(url)

print(r.status_code)