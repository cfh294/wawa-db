# coding: utf-8
import datetime
from sqlalchemy import Column, Numeric, String, Integer, Boolean, DateTime, Time, ForeignKey, MetaData
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base(MetaData(schema="wawamgr"))
metadata = Base.metadata



class Wawa(Base):
    __tablename__ = "wawa"
    __table_args__ = {"schema" : "wawamgr"}

    id = Column(Integer, primary_key=True, nullable=False)
    location_id = Column(Integer, nullable=False)
    has_menu = Column(Boolean, nullable=False)
    last_updated = Column(DateTime, nullable=False)
    open_24_hours = Column(Boolean, nullable=False)
    regional_director = Column(String(1000))
    store_close = Column(Time, nullable=False)
    store_name = Column(String(1000), nullable=False)
    store_number = Column(Integer, nullable=False)
    store_open = Column(Time, nullable=False)
    telephone = Column(String(20))
    address = Column(String(1000))
    city = Column(String(1000))
    state = Column(String(2))
    zip = Column(String(5))
    longitude = Column(Numeric, nullable=False)
    latitiude = Column(Numeric, nullable=False)
    geom = Column(Geometry("Point"))
    has_food = Column(Boolean, nullable=False)
    has_fuel = Column(Boolean, nullable=False)
    has_restrooms = Column(Boolean, nullable=False)
    has_ethanol_free_gas = Column(Boolean, nullable=False)
    has_tesla_charging_station = Column(Boolean, nullable=False)
    
    gas_prices = relationship("GasPrice", back_populates="wawa")
    

class GasType(Base):
    __tablename__ = "gas_type"
    __table_args__ = {"schema" : "wawamgr"}
    
    id = Column(String(10), nullable=False, primary_key=True)
    description = Column(String(500), nullable=False)
    

class GasPrice(Base):
    __tablename__ = "gas_price"
    __table_args__ = {"schema" : "wawamgr"}
    
    id = Column(Integer, primary_key=True, nullable=False)
    gas_type_id = Column(String(10), ForeignKey("wawamgr.gas_type.id"))
    gas_type = relationship("GasType")
    
    wawa_id = Column(Integer, ForeignKey("wawamgr.wawa.id"))
    wawa = relationship("Wawa", back_populates="gas_prices")
    
    update_date = Column(DateTime, default=datetime.datetime.now())