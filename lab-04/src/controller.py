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
  def get_quote(id=None, text=None, author=None, category=None, tag=None, popularity=None, offset=0, limit=10):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    if not id or id == 0: 
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
      if not id:        
        return result.order_by(Quote.id).offset(offset).limit(limit)
      else:
        return result.order_by(func.random()).first()
    else:
      return session.query(Quote).get(id)