from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import and_, or_

from genera_base import Pais 
  
engine = create_engine('sqlite:///basepais.db') 
  
Session = sessionmaker(bind=engine) 
session = Session() 
  
  
paises = session.query(Pais.pais).filter(or_(Pais.pais.like("%uador"), Pais.capital.like("%ito"))).order_by(Pais.pais).all()
print(paises)