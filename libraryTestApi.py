import requests
from utilities.payload import *
from utilities.endpoints import *

headers = {'Content-Type': 'application/json'}
post_response = requests.post(ApiEndpoints.addBook, json=addBook(), headers=headers,)
resp_json = post_response.json()
print(post_response.json())
bookId = resp_json['ID']

get_response = requests.get(ApiEndpoints.getBook, params={'ID': bookId},)
print(get_response.text)
list_resp = get_response.json()
print(list_resp[0]['author'])
assert get_response.status_code == 200
assert 'application/json' in get_response.headers['Content-Type']

get_response = requests.get(ApiEndpoints.getBook, params={'AuthorName': 'Rahul Shetty'},)
# print(response.text)
list_resp = get_response.json()
assert get_response.status_code == 200
expectedIsbn = 'gahuhgag'

for actualBook in list_resp:
    if actualBook['isbn'] == expectedIsbn:
        print(actualBook)
        break

expectedBook = {
        "book_name": "Book-337e5a4f-9797-4fc9-8162-e4e6befc6c91",
        "isbn": "gahuhgag",
        "aisle": "4253"
    }

assert actualBook == expectedBook

del_response = requests.post(ApiEndpoints.deleteBook, json=
{
    "ID": bookId
}, headers={'Content-Type': 'application/json'},)
assert del_response.status_code == 200
assert del_response.json()['msg'] == 'book is successfully deleted'
print(del_response.json())
