import pymongo
import json

def read_config_properties():
    prop = {}
    with open('config.properties', 'rt') as f:
        for line in f:
            key, value = line.strip().split('=')
            prop[key] = value
    return prop

prop = read_config_properties()
user     = prop['user']
password = prop['password']
server   = prop['server']
client = pymongo.MongoClient(f'mongodb+srv://{user}:{password}@{server}/?retryWrites=true&w=majority')
collection = client.quotes.quotes
# load 10K quotes data
count = 0
with open('db/quotes.json', 'rt') as f: 
    quotes = json.load(f)
    for quote in quotes:
        count += 1
        new_quote = {}
        new_quote['_id'] = count
        new_quote['text'] = quote['Quote']
        new_quote['author'] = quote['Author']
        new_quote['popularity'] = quote['Popularity']
        new_quote['category'] = quote['Category']
        new_quote['tags'] = quote['Tags']
        collection.insert_one(new_quote)
        if count == 10000:
            break
client.close()