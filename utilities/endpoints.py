from utilities.configurations import *


class ApiEndpoints:
    config = getConfig()
    uri = config['API']['endpoint'] + '/Library/'
    addBook = uri + 'Addbook.php'
    deleteBook = uri + 'DeleteBook.php'
    getBook = uri + 'GetBook.php'
