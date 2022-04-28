import sqlite3
import json

conn = sqlite3.connect('db/quotes.db')

with open('db/quotes.sql') as f:
    conn.executescript(f.read())

conn.commit()

# load 10K quotes data
cur = conn.cursor()
count = 0
with open('db/quotes.json', 'rt') as f: 
    quotes = json.load(f)
    for quote in quotes:
        text = quote['Quote']
        author = quote['Author']
        popularity = quote['Popularity']
        category = quote['Category']
        sql = 'INSERT INTO quotes (text, author, popularity, category) VALUES ( ?, ?, ?, ? )'
        cur.execute(sql, [text, author, popularity, category])
        id = cur.lastrowid
        tags = quote['Tags']
        for tag in tags:
            try:
                sql = 'INSERT INTO quote_tags VALUES ( ?, ? )'
                cur.execute(sql, [id, tag])
            except Exception: 
                pass
        conn.commit()
        count += 1
        # if count % 100 == 0:
        #     print(count)
        if count == 10000:
            break

sql = 'SELECT COUNT(*) FROM quotes'
cur.execute(sql)
row = cur.fetchone()
print(row[0], 'quotes inserted!')

conn.close()