from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///equipment.db', echo=True)
Base = declarative_base()


class Equipment(Base):
    """"""
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    itemcode = Column(String)
    typee=Column(String)
    rangee = Column(String)
    make=Column(String)
    procdate=Column(String)
    source=Column(String)
    accept=Column(String)
    lc = Column(String)
    freq=Column(String)
    stock=Column(String)
    center=Column(String)
    locid=Column(String)
    status = Column(String)
    #lastissue=Column(String)
    #creationdate=Column(String)
    #lastedit=Column(String)
    ticketno=Column(String)
    empname=Column(String)
    ngmin=Column(String)
    ngmax=Column(String)
    gumin=Column(String)
    gumax=Column(String)
    nogmin=Column(String)
    nogmax=Column(String)
    sizemin=Column(String)
    sizemax=Column(String)

class History(Base):
    """"""
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    itemcode = Column(String)
    masterref=Column(String)
    chkdate=Column(String)
    calibby=Column(String)
    remarks=Column(String)
    nextcalib=Column(String)
    sd1=Column(String)
    sd2=Column(String)
    sd3=Column(String)
    sd4=Column(String)
    sd5=Column(String)
    od1=Column(String)
    od2=Column(String)
    od3=Column(String)
    od4=Column(String)
    od5=Column(String)
    gmajd1=Column(String)
    ngmajd1=Column(String)
    geffd1=Column(String)
    ngeffd1=Column(String)
    gpitd1=Column(String)
    ngpitd1=Column(String)
    gpitd2=Column(String)
    ngpitd2=Column(String)
    gmajd2=Column(String)
    ngmajd2=Column(String)
    geffd2=Column(String)
    ngeffd2=Column(String)

# create tables
Base.metadata.create_all(engine)
