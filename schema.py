from pydantic import BaseModel


class CreateAddressBook(BaseModel):
    add_lattitude: float
    add_longitude: float
    address_des: str
    user_lattitude: float
    user_longitude: float

class UpdateAddressBook(BaseModel):
    add_lattitude: float
    add_longitude: float
    address_des: str
    user_lattitude: float
    user_longitude: float