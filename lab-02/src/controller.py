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
  def get_quote(id):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    return result.order_by(func.random()).first() if id == 0 else result.get(id)