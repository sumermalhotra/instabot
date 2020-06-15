""" This file is used to accept username and password credentials for the user """

class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

# Enter username and password respectively in the quotations
acc = Account('', '')