from fastapi import FastAPI, APIRouter, Depends, HTTPExecption
from sqlalchemy.orm import Session

import models
from schema import CreateAddressBook, UpdateAddressBook
from database import get_db

from distance_calc import distance_calculator

router = APIRouter(prefix="/address", tags=["Address"])

@router.post("/add")
def create_address_book(address:CreateAddressBook, db:Session = Depends(get_db)):
    address_model = models.AddressBook()
    address_model.address_des = address.address_des
    address_model.add_lattitude = address.add_lattitude
    address_model.add_longitude = address.add_longitude
    db.add(address_model)
    db.commit()
    return address

@router.put("/update")
def update_address_book(address:UpdateAddressBook, id:int, db:Session = Depends(get_db)):
    address_model = db.query(models.AddressBook).filter(models.AddressBook.id==id).first()
    if address_model:
        address_model.address_des = address.address_des
        address_model.add_lattitude = address.add_lattitude
        address_model.add_longitude = address.add_longitude
        db.add(address_model)
        db.commit()
        return address
    else:
        raise HTTPExecption(
            status_code=404,
            details=f"book {id}: Does not exist"
        )
    
@router.delete("/delete/{add_id}")
def update_address_book(add_id:int, db:Session = Depends(get_db)):
    address_model = db.query(models.AddressBook).filter(models.AddressBook.id==add_id).first()
    if address_model is None:
        raise HTTPExecption(
            status_code=404,
            details=f"book {id}: Does not exist"
        )
    else:
        db.query(models.AddressBook).filter(models.AddressBook.id==add_id).delete()
        db.commit()
        return {"message": "address deleted!!"}
    
@router.get("/get_addresses")
def get_address_within_distance(user_lat:float, user_lon:float, distance:int, db:Session=Depends(get_db)):
    address_model = db.query(models.AddressBook).all()
    result = []
    for address in address_model:
        dist = distance_calculator(user_lat, user_lon, address["add_lattitude"], address["add_longitude"])
        if dist<=distance:
            result.append(address)
    return result






