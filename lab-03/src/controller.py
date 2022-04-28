from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from .models import Quote

class Controller: 

  engine = None

  @staticmethod
  def get_engine():
    if not Controller.engine: 
      Controller.engine = create_engine('sqlite:///db/quotes.db')
    return Controller.engine
    
  # NOTE: following method has been modified
  @staticmethod
  def get_quote(id, text=None, author=None, category=None, tag=None, popularity=None):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    if id == 0: 
      result = session.query(Quote)
      if text: 
        result = result.filter(Quote.text.contains(text))
      if author:
        result = result.filter(Quote.author.contains(author))
      if category: 
        result = result.filter(Quote.category == category)
      if popularity: 
        result = result.filter(Quote.popularity >= popularity)
      if tag: 
        result = result.filter(Quote.tags.any(tag=tag))
      quote = result.order_by(func.random()).first()
    else:
      quote = session.query(Quote).get(id)
    return quote