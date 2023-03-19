import random
import string


def addBook():
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": "babshi",
        "aisle": random.choice(string.ascii_lowercase) + str(random.randint(1000, 10000)),
        "author": "Jawani Adich"
    }
    return body
