# Reads in the token from token.txt located in local directory

def read_token():
    token_file = open('token.txt','r')
    token = token_file.read()
    return token

def read_db_url():
    db_f = open('db_url.txt','r')
    url = db_f.read()
    return url
