#  create a database to store the url & the hashed values 

import sqlite3

create_table = """
CREATE TABLE url_shorten (
 base_url TEXT UNIQUE,  
 short_url TEXT UNIQUE
);
"""

with sqlite3.connect('url.db') as conn:
    cur = conn.cursor()
    cur.execute(create_table)