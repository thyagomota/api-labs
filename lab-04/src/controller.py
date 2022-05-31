from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from .models import Quote
import copy

class Controller: 

  engine = None

  @staticmethod
  def get_engine():
    if not Controller.engine: 
      Controller.engine = create_engine('sqlite:///db/quotes.db?check_same_thread=False')
    return Controller.engine
    
  @staticmethod
  def get_quotes_id(id):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    quote = result.order_by(func.random()).first() if id == 0 else result.get(id)
    return quote

  @staticmethod
  def get_quotes(text=None, author=None, category=None, tag=None, popularity=None, offset=0, limit=10):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    if text: 
      result = result.filter(Quote.text.contains(text))
    if author:
      result = result.filter(Quote.author.contains(author))
    if category: 
      result = result.filter(Quote.category == category)
    if popularity: 
      result = result.filter(Quote.popularity >= float(popularity))
    if tag: 
      result = result.filter(Quote.tags.any(tag=tag))
    result = result.offset(offset).limit(limit)
    return [r for r in result]