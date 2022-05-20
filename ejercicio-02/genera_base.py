from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepais.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'pais'
    
    id = Column(Integer, primary_key=True)
    pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname = Column(String)
    itu = Column(String)
    lenguaje = Column(String)
    independiente = Column(String)

def __repr__(self):
        return "Pais: Pais=%s Capital=%s Continente:%s Dial=%s Geoname ID=%s ITU:%s \
        Lenguajes=%s Independiente=%s" % (
                          self.pais,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.geoname,
                          self.itu,
                          self.lenguaje,
                          self.independiente)

Base.metadata.create_all(engine)






