from sqlalchemy import create_engine

class DBHelper: 

  engine = None

  @staticmethod
  def get_engine():
    if not DBHelper.engine: 
      DBHelper.engine = create_engine('sqlite:///db/quotes.db')
    return DBHelper.engine
