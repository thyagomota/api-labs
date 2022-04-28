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
    
  @staticmethod
  def get_quote(tag=None):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    if tag: 
      quote = session.query(Quote).filter(Quote.tags.any(tag=tag)).order_by(func.random()).first()
    else:
      quote = session.query(Quote).order_by(func.random()).first()
    return quote