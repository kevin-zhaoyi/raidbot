# Reads in the token from token.txt located in local directory

def read_token():
    token_file = open('token.txt','r')
    token = token_file.read()
    return token