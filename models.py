from sqlalchemy import Column, Integer, String, Float
from database import Base


class AddressBook(Base):
    __tablename__ = "addbook"

    id = Column(Integer, primary_key=True, index=True)
    address_des = Column(String, index=True)
    add_lattitude = Column(Float, index=True)
    add_longitude = Column(Float, index=True)
