import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'ID': 'babshi001'},)
print(response.text)
list_resp = response.json()
print(list_resp[0]['author'])
assert response.status_code == 200
assert 'application/json' in response.headers['Content-Type']
