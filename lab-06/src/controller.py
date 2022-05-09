import pymongo

def read_config_properties():
    prop = {}
    with open('config.properties', 'rt') as f:
        for line in f:
            key, value = line.strip().split('=')
            prop[key] = value
    return prop

class Controller: 

  client = None

  @staticmethod
  def get_client():
    if not Controller.client: 
      prop = read_config_properties()
      user     = prop['user']
      password = prop['password']
      server   = prop['server']
      Controller.client = pymongo.MongoClient(f'mongodb+srv://{user}:{password}@{server}/?retryWrites=true&w=majority')
    return Controller.client

  @staticmethod
  def get_quote():
    client = Controller.get_client()
    db = client.quotes
    quotes = db.quotes
    pipeline = [
      {'$sample': {'size': 1}}
    ]
    quote = quotes.aggregate(pipeline).next()
    return quote