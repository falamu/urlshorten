import string
import random
import sqlite3

def shortener(url, alias=None):
    '''
    enter a url and return the shortened url
    '''

    def _shorten(url, alias=None):
        
        if alias:
            shortened_url = alias
            
        else: 
            # generate 8-10 character alphanumeric string based on randomly selected numbers
            alphabet = string.ascii_letters + string.digits
            chars = len(alphabet) - 1
            DEFAULT_LENGTH = random.randint(8,10)
            encode = []
            for _ in range(DEFAULT_LENGTH):
                num = random.randint(0, chars)
                encode.append(num)
            
            shortened_url = ''.join(alphabet[char] for char in encode)
        update_stmt = f"insert into url_shorten(base_url, short_url) values ('{url}', '{shortened_url}');"
        
        try:
            with sqlite3.connect('url.db') as conn:
                cur = conn.cursor()
                cur.execute(update_stmt)
                conn.commit()
        
        except Exception as e:
            print(e)
            _shorten(url)
        return shortened_url

    check_shortened_urls(url, check_type='base')

    if alias: 
        check_shortened_urls(alias, check_type = 'alias')
        shortened_url = _shorten(url, alias)

    else:
        shortened_url = _shorten(url)

    return shortened_url


def check_shortened_urls(url, check_type):
    ''' 
    checks if url has already been shortened 
    '''
    table = 'url_shorten'
    
    if check_type == 'base':
        field = 'base_url'
    elif check_type == 'alias': 
        field = 'short_url'
    else:
        raise TypeError('check type must be either `url` or `alias`')

    with sqlite3.connect('url.db') as conn:
        check_url_stmt = f"SELECT * FROM {table} WHERE {field} = '{url}'"
        cur = conn.cursor()
        response = cur.execute(check_url_stmt)
        result = response.fetchone()
    
    if result is None:
        return 
    else: 
        raise Exception(f'{field} {url} already exists')