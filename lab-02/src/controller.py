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
  def get_quote(id):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    if id == 0:
      quote = result.order_by(func.random()).first()
    else:
      quote = result.get(id)
    return quote